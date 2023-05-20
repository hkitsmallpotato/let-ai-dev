from llama_cpp import Llama
import gradio as gr

llm = Llama(model_path="./wizard-mega-13B.ggml.q4_0.bin", n_ctx=1500) #, n_gpu_layers=40

# TODO: Whatever works atm
def run_llm(prompt):
    output = llm(prompt, max_tokens=12, stop=["Q:", "[end of text]"], echo=True)
    prefix_l = len(prompt)
    return output['choices'][0]['text'][prefix_l:]

# TODO: Also just copied from quickstart doc
copyediting = { "intro": """# Auto Software Dev Demo 
This is a Proof-of-concept for using LLM to automate the SDLC. 

*Important Caveat: No quality gaurantee, it may fail completely.*
"""}

with gr.Blocks() as software_dev_app:
    gr.Markdown(copyediting["intro"])
    with gr.Tab("System Design"):
        with gr.Column(scale=1):
            initial_prompt = gr.Textbox(label="Initial Prompt")
        with gr.Column(scale=1):
            output = gr.Textbox(label="AI reply")
            ask_btn = gr.Button("Ask AI!")
            ask_btn.click(fn=run_llm, inputs=initial_prompt, outputs=output, api_name="ask")
    with gr.Tab("App scaffolding"):
        gr.Markdown("Under construction!")
software_dev_app.launch()
