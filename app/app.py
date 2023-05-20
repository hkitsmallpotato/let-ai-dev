from llama_cpp import Llama
import gradio as gr

llm = Llama(model_path="./wizard-mega-13B.ggml.q4_0.bin", n_ctx=1500) #, n_gpu_layers=40

# TODO: Whatever works atm
def run_llm(prompt):
    output = llm(prompt, max_tokens=12, stop=["Q:", "[end of text]"], echo=True)
    prefix_l = len(prompt)
    return output['choices'][0]['text'][prefix_l:]

# TODO: Also just copied from quickstart doc
with gr.Blocks() as software_dev_app:
    initial_prompt = gr.Textbox(label="Initial Prompt")
    output = gr.Textbox(label="AI reply")
    ask_btn = gr.Button("Ask AI!")
    ask_btn.click(fn=run_llm, inputs=initial_prompt, outputs=output, api_name="ask")

software_dev_app.launch()
