#Augmented chatbot UI

import gradio as gr
import random
import time

with gr.Blocks() as demo:
    action_history = gr.State(value=[])
    actions = gr.Markdown(value="")
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    #eg = gr.Examples(["What is the implication of expired debt ceiling?", \
    #                  "Are there instances of government deadlock in history?", \
    #                  "Why is the US reaching the debt ceiling again?"],\
    #                 msg)
    followups = gr.Dataset(components=[gr.Textbox(visible=False)],\
                          label="Follow-up questions",\
                          samples=[["What is the implication of expired debt ceiling?"],\
                                   ["Are there instances of government deadlock in history?"],\
                                   ["Why is the US reaching the debt ceiling again?"]])
    def on_select(evt: gr.SelectData):
        return evt.value[0]
    followups.select(fn=on_select, inputs=None, outputs=msg)\
            .success(fn=dothings, inputs=action_history, outputs=[action_history, actions])\
            .success(fn=respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    clear = gr.ClearButton([msg, chatbot])
    def gen_sample():
        return [["Hello"], ["world"]]
    load_sample = gr.Button("Testing").click(fn=gen_sample, outputs=followups)

    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history
    
    def render_actions(hist):
        s = "# Actions\n"
        for a in hist:
            if a["type"] == "search":
                s += "- Searching on the web for **{query}**\n".format(query=a["v"])
            elif a["type"] == "visit":
                s += "- Visiting website **{title}**\n".format(title=a["v"])
        return s
    def dothings(hist):
        a = random.choice([{"type":"search", "v":"How to make a cake"}, {"type":"visit", "v":"Quick and easy cake recipe - Etsy"}])
        hist.append(a)
        return hist, render_actions(hist)
    msg.submit(dothings, action_history, [action_history, actions]).success(respond, [msg, chatbot], [msg, chatbot])

demo.launch(share=True)
