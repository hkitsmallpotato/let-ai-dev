import requests
import html2text
from gradio_client import Client
import jinja2
import time
import re

import gradio as gr

c = Client("https://openaccess-ai-collective-manticore-13b-chat-pyg.hf.space/")
text_maker = html2text.HTML2Text()
text_maker.ignore_links = True
text_maker.ignore_images = True


def ask_llm(prompt, c):
    job = c.submit(prompt, api_name="/predict")
    while not job.done():
        print(job.status())
        time.sleep(5)
    return job.outputs()[-1]

#action_regex = "Action:[ ]*(search_internet|visit_website)\(\"?(.*)\"?\)"
action_regex = "(search_internet|visit_website)\(\"?(.*)\"?\)"


# data is list of [url, title snippet]
def do_web_search(query):
    req = requests.get("https://tailsx.com/api", params={'q':query,'t':'text','api':'true'})
    j = req.json()
    return {"md": "\n".join([ "{n}. [{title}]({url})\n{snippet}".format(title = x[1], url = x[0], snippet = x[2], n = i+1) for (i, x) in enumerate(j)]), "data": j }

def grab_webpage(url, text_maker):
    req = requests.get(url)
    return text_maker.handle(req.text)

def load_jinja_templates(base, templates):
    templateLoader = jinja2.FileSystemLoader(searchpath=base)
    templateEnv = jinja2.Environment(loader=templateLoader)
    loaded_templates = {}
    for name, templ in templates.items():
        loaded_templates[name] = templateEnv.get_template(templ)
    return loaded_templates

prompts = load_jinja_templates("./prompts",{"initial":"initial.md", "index_map":"index_map.md", "index_reduce":"index_reduce.md"})

#prompts["initial"].render(question="Hello", steps = [], hint="")

#re.search( action_regex, raw_a[-1])[2]

def detect_action(string):
    result = re.search(action_regex, string)
    if result is not None:
        return {"found": True, "whole":result[0], "action_type":result[1], "action_arg":result[2] }
    else:
        return {"found": False }

def consolidate_doc_from_url(url, q):
    doc = grab_webpage(url, text_maker)
    print(doc)
    chunks, chunk_size = len(doc), 3 * 1400
    chunked_doc = [ doc[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
    summaries = []
    for chunk in chunked_doc:
        print(chunk)
        p = prompts["index_map"].render(question=q, snippet=chunk)
        summaries.append(ask_llm(p, c))
    p = prompts["index_reduce"].render(question=q, snippets=summaries)
    print(p)
    ans = ask_llm(p, c)
    return ans

# Main loop?

class TracedChatbot:
    def __init__(self, q):
        self.p = ""
        self.q = q
        self.raw_answers = []
        self.web_search_history = []
    
    def run_one_iteration(self, guidiance):
        self.p = prompts["initial"].render(question=self.q, steps=self.raw_answers, hint=guidiance)
        self.raw_answers.append(ask_llm(self.p, c))
    
    def remove_last_answer(self):
        del self.raw_answers[-1]
    
    def merge_last_two(self, newline):
        tempA = self.raw_answers[-2]
        tempB = self.raw_answers[-1]
        del self.raw_answers[-1]
        del self.raw_answers[-1]
        if newline:
            s = "\n"
        else:
            s = ""
        self.raw_answers.append(tempA + s + tempB)
    
    def add_search_result(self, search_query):
        self.web_search_history.append(do_web_search(search_query))
        self.raw_answers.append("System Reply:\nYour web search returned these results:\n" + self.web_search_history[-1]["md"])


#------------------------------------------------


def ui_run_step(uistate_chatbot, ui_question, ui_guidiance):
    if uistate_chatbot is None:
        chatbot = TracedChatbot(ui_question)
    else:
        chatbot = uistate_chatbot
    chatbot.run_one_iteration(ui_guidiance + " ")
    return chatbot

def ui_feed_response(uistate_chatbot):
    return [[ans] for ans in uistate_chatbot.raw_answers]

def ui_detect_action(ui_bot_steps):
    print(ui_bot_steps[-1])
    res = detect_action(ui_bot_steps[-1][0])
    if res["found"]:
        print(res["whole"])
        mapV = { "search_internet": "Search Internet", "visit_website": "Visit Website" }
        return (mapV[res["action_type"]], res["action_arg"])
    else:
        return ("", "")

def ui_do_action(uistate_chatbot, ui_action_type, ui_action_arg):
    if ui_action_type == "Search Internet":
        uistate_chatbot.add_search_result(ui_action_arg)
        return (uistate_chatbot.web_search_history[-1]["data"], uistate_chatbot.web_search_history[-1]["md"])
    else:
        return ([], "")

# TODO: hardcoded help text
help_text = """# Trace a chatbot

*(This help text is co-written by the Manticore-13B AI)*

Welcome to this demo app that helps you understand how a tooling-enhanced, LLM-powered AI chatbot works! The agent uses ReACT technique in prompt engineering and tool use integration in a loop to power a chatbot that can search and read internet to get up-to-date information to answer user queries.  You can refer to the GitHub repository at [hkitsmallpotato/let-ai-dev](https://github.com/hkitsmallpotato/let-ai-dev) for source code.

## UI Organization

There are five tabs: 
- Help - this tab
- System Trace - The main tab, divided into three areas:
  - Panel to trigger one step of asking LLM
  - Panel showing history of AI response and to edit/correct it
  - Panel to trigger tool actions
- Web Search - Shows result of the last internet search
- Indexing - show internals of article summarization using LLM through chunking
- System Prompt - let user experiment with different prompts to improve the AI's output quality/instruction-following ability.

Note:
- There are two possible tool action that can be triggered by the chatbot: Web Search and Indexing.
- The reason indexing is needed is because of the context length limit, and most internet articles are longer than that. We solve this by chunking it into pieces, feed each small piece to LLM asking it to give a summary relevant to the user question, then run one more pass over the LLM with these summary to produce a final snippet.

## How to use

To step through the execution of the AI agent, follow these steps:

1. Enter your query in the text box provided.
2. The guidance feature will force the first word of the AI's response to guide it.
3. Click on "Ask AI" to get a response from the chatbot.
4. You can edit, delete or merge the last two responses in the response panel.
5. Once you have the desired output, click on "Detect action" to detect the formatted output in the "Action" field of the AI's last response.
6. The system will auto-fill the action type and argument fields based on the detected format.
7. Click on "Execute action" to execute the action with the resulting information pasted as a “System reply” in the response panel.
8. You can then loop back to step 3 for further interactions with the AI agent.

## Reference

TODO
"""



with gr.Blocks() as trace_chatbot:
    with gr.Tab("Help"):
        gr.Markdown(help_text)
    with gr.Tab("Trace Chatbot"):
        uistate_chatbot = gr.State()
        with gr.Row():
            with gr.Column():
                ui_action_history = gr.Markdown("## Action History: \n*None*")
                ui_bot_steps = gr.Dataframe(headers=["Chatbot Output"], \
                                            datatype=["str"], \
                                            col_count=(1, "fixed"), \
                                            type="array", value=[["Hello"], ["bye"]], interactive=True)
                btn_detect_action = gr.Button(value="Detect Action")
                btn_remove_last = gr.Button(value="Remove last")
                btn_merge = gr.Button(value="Merge last two")
            with gr.Column():
                with gr.Box():
                    ui_question = gr.Textbox(label="User Question")
                    ui_guidiance = gr.Radio(["None", "Observation:", "Thought:", "Action:"], label="Guidiance")
                    btn_ask = gr.Button(value="Run one LLM Step")
                    btn_ask.click(fn=ui_run_step, inputs=[uistate_chatbot, ui_question, ui_guidiance], outputs=[uistate_chatbot]) \
                           .success(fn=ui_feed_response, inputs=uistate_chatbot, outputs=ui_bot_steps)
                    ui_ai_output = gr.Textbox(label="AI Output")
                with gr.Box():
                    ui_action_type = gr.Dropdown(["Search Internet", "Visit Website"], label="Action type", interactive=True)
                    ui_action_arg = gr.Textbox(label="Action Argument", interactive=True)
                    btn_perform_action = gr.Button(value="Do action")
                    btn_detect_action.click(fn=ui_detect_action, inputs=ui_bot_steps, outputs=[ui_action_type, ui_action_arg])
    with gr.Tab("Web Search"):
        gr.Markdown("Under Construction")
        with gr.Row():
            with gr.Column():
                ui_websearch_data = gr.Dataframe(headers=["URL", "Title", "Snippet"], \
                                            datatype=["str", "str", "str"], \
                                            col_count=(3, "fixed"), \
                                            type="array")
            with gr.Column():
                ui_websearch_md = gr.Markdown()
            btn_perform_action.click(fn=ui_do_action, inputs=[uistate_chatbot, ui_action_type, ui_action_arg], outputs=[ui_websearch_data, ui_websearch_md])
    with gr.Tab("System Prompt"):
        gr.Markdown("Under Construction")


trace_chatbot.queue().launch()


