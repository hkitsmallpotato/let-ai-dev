from llama_cpp import Llama
import gradio as gr

from huggingface_hub import hf_hub_download

import zipfile

# Cutting edge model doesn't work due to recent compatibility breakage and too fast to catch up downstream
# Expect things to break a lots
# TODO: Add reference to gh issue
our_model_path = hf_hub_download(repo_id="TheBloke/wizard-mega-13B-GGML", filename="wizard-mega-13B.ggml.q4_0.bin", revision="previous_llama_ggmlv2")

# "./wizard-mega-13B.ggml.q4_0.bin"
llm = Llama(model_path=our_model_path, n_ctx=1500) #, n_gpu_layers=40

# TODO: Whatever works atm
def run_llm(prompt, max_token):
    output = llm(prompt, max_tokens=max_token, stop=["Q:", "[end of text]"], echo=True)
    prefix_l = len(prompt)
    return output['choices'][0]['text'][prefix_l:]
def run_llm_stream(prompt, max_token):
    outputs = llm(prompt, max_tokens=max_token, \
                 stop=["Q:", "[end of text]", "</s>"], \
                 echo=True, stream=True)
    text = ""
    for output in outputs:
        tok = output['choices'][0]['text']
        text = text + tok
        yield text

# Temporary hack to load prompts
system_prompts = {}
promptset = [("init", "prompt_initial.md"), ("req", "prompt_requirement.md"), ("name", "prompt_name.md")]
for prompt_key, filename in promptset:
    with open(filename, "r") as f:
        system_prompts[prompt_key] = f.read()


file_generated = ["user_out_init.md", "user_out_name.md", "user_out_req.md"]

def update_asset(download_assets, ses_state, text):
    cur_file_name = file_generated[ses_state]
    with open(cur_file_name, "w") as f:
        f.write(text)
    return (file_generated[:ses_state + 1], ses_state + 1)

# ... and have a static flow graph etc
def run_initial(user_statement, is_streaming, max_token):
    p = system_prompts["init"].format(product=user_statement)
    if is_streaming:
        stream = run_llm_stream(p, max_token)
        for current_output in stream:
            yield current_output
    else:
        result = run_llm(p, max_token)
        yield result

def run_req(summary, is_streaming, max_token):
    p = system_prompts["req"].format(sum=summary)
    if is_streaming:
        stream = run_llm_stream(p, max_token)
        for current_output in stream:
            yield current_output
    else:
        result = run_llm(p, max_token)
        yield result

def run_name(summary, is_streaming, max_token):
    p = system_prompts["name"].format(sum=summary)
    if is_streaming:
        stream = run_llm_stream(p, max_token)
        for current_output in stream:
            yield current_output
    else:
        result = run_llm(p, max_token)
        yield result



def gen_zipfile(dummy):
    with zipfile.ZipFile("user_out_all.zip", mode="w") as archive:
        for filename in ["user_out_init.md", "user_out_name.md", "user_out_req.md"]:
            archive.write(filename)
    return ["user_out_init.md", "user_out_name.md", "user_out_req.md", "user_out_all.zip"]

# TODO: Also just copied from quickstart doc
copyediting = { "intro": """# Auto Software Dev Demo 
This is a Proof-of-concept for using LLM to automate the SDLC. 

*Important Caveat: No quality gaurantee, it may fail completely.*
"""}

with gr.Blocks() as software_dev_app:
    gr.Markdown(copyediting["intro"])
    with gr.Tab("System Design"):
        ses_state = gr.State(0)
        with gr.Row():
            with gr.Column(scale=1):
                initial_prompt = gr.Textbox(label="Initial Prompt", info="What do you want to build?")
                is_streaming = gr.Checkbox(label="Streaming output?", value=True)
                max_token = gr.Slider(20, 1000, value=300, label="Max Token")
                ask_btn = gr.Button("Ask AI now!")
            with gr.Column(scale=1):
                with gr.Accordion(label="Requirement Analysis", open=True):
                    output1 = gr.Textbox(label="Initial analysis")
                    output2 = gr.Textbox(label="Project name and summary")
                    output3 = gr.Textbox(label="Requirement Analysis")
                with gr.Accordion(label="System Architecture", open=False):
                    output4 = gr.Textbox(label="")
                with gr.Accordion(label="Frontend Design", open=False):
                    output5 = gr.Textbox(label="")
                    output6 = gr.Textbox(label="")
                with gr.Accordion(label="Backend Design", open=False):
                    output7 = gr.Textbox(label="")
        with gr.Row():
            gr.Markdown("Test")
            download_assets = gr.Files(label="Download Documents", value=[])
        ask_btn.click(fn=run_initial, inputs=[initial_prompt, is_streaming, max_token], outputs=output1) \
          .success(fn=update_asset, inputs=[download_assets, ses_state, output1], outputs=[download_assets, ses_state]) \
          .success(fn=run_name, inputs=[output1, is_streaming, max_token], outputs=output2) \
          .success(fn=update_asset, inputs=[download_assets, ses_state, output2], outputs=[download_assets, ses_state]) \
          .success(fn=run_req, inputs=[output1, is_streaming, max_token], outputs=output3) \
          .success(fn=update_asset, inputs=[download_assets, ses_state, output3], outputs=[download_assets, ses_state]) \
          .success(fn=gen_zipfile, inputs=download_assets, outputs=download_assets)
    with gr.Tab("App scaffolding"):
        gr.Markdown("Under construction!")

software_dev_app.queue().launch() # queue needed for respond time > 60 sec
