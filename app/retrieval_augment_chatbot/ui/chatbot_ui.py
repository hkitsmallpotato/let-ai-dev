#Augmented chatbot UI

import gradio as gr
import random
import time

with gr.Blocks() as demo:
    action_history = gr.State(value=[])
    actions = gr.Markdown(value="")
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    
    followups = gr.Dataset(components=[gr.Textbox(visible=False)],\
                          label="Follow-up questions",\
                          samples=[["What is the implication of expired debt ceiling?"],\
                                   ["Are there instances of government deadlock in history?"],\
                                   ["Why is the US reaching the debt ceiling again?"]])

    def on_select(evt: gr.SelectData):
        return evt.value[0]
    
    followups.select(fn=on_select, inputs=None, outputs=msg)\
            .success(fn=dothings, inputs=[action_history, chatbot], outputs=[action_history, actions])\
            .success(fn=respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    clear = gr.ClearButton([msg, chatbot])

    def gen_sample():
        return [["Hello"], ["world"]]
    
    load_sample = gr.Button("Testing").click(fn=gen_sample, outputs=followups)

    def respond(message, chat_history):
        bot_message = convAgent.generate_response()
        chat_history.append((message, bot_message))
        convAgent.resetThoughts()
        return "", chat_history
    
    def render_actions(hist):
        s = "# Actions\n"
        for a in hist:
            if a["type"] == "search":
                s += "- Searching on the web for **{query}**\n".format(query=a["v"])
            elif a["type"] == "visit":
                s += "- Visiting website **{title}**\n".format(title=a["v"])
        return s
    def dothings(hist, chat_history):
        convAgent.setContext(chat_history)
        next_action = convAgent.think()
        while next_action["type"] != "final_answer":
            hist.append(next_action)
            yield (hist, render_actions(hist))
            action_result = executorAgent.executeAction(next_action)
            convAgent.appendObservation(action_result)
            convAgent.think()
    
    msg.submit(dothings, [action_history, chatbot], [action_history, actions]).success(respond, [msg, chatbot], [msg, chatbot])

demo.launch(share=True)
