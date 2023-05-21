from llama_cpp import Llama
import gradio as gr

from huggingface_hub import hf_hub_download

# Cutting edge model doesn't work due to recent compatibility breakage and too fast to catch up downstream
# Expect things to break a lots
# TODO: Add reference to gh issue
our_model_path = hf_hub_download(repo_id="TheBloke/wizard-mega-13B-GGML", filename="wizard-mega-13B.ggml.q4_0.bin", revision="previous_llama_ggmlv2")

# "./wizard-mega-13B.ggml.q4_0.bin"
llm = Llama(model_path=our_model_path, n_ctx=1500) #, n_gpu_layers=40

# TODO: Whatever works atm
def run_llm(prompt):
    output = llm(prompt, max_tokens=12, stop=["Q:", "[end of text]"], echo=True)
    prefix_l = len(prompt)
    return output['choices'][0]['text'][prefix_l:]

# Temporary hack to load prompts
system_prompts = {}
promptset = [("init", "prompt_initial.md"), ("req", "prompt_requirement.md"), ("name", "prompt_name.md")]
for prompt_key, filename in promptset:
    with open(filename, "r") as f:
        system_prompts[prompt_key] = f.read()

# ... and have a static flow graph etc
def run_initial(user_statement):
    p = system_prompts["init"].format(product=user_statement)
    return run_llm(p)

def run_req(summary):
    p = system_prompts["req"].format(sum=summary)
    return run_llm(p)

def run_name(summary):
    p = system_prompts["name"].format(sum=summary)
    return run_llm(p)


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
            output1 = gr.Textbox(label="AI reply 1")
            output2 = gr.Textbox(label="AI reply 2")
            output3 = gr.Textbox(label="AI reply 3")
            ask_btn = gr.Button("Ask AI!")
            ask_btn.click(fn=run_initial, inputs=initial_prompt, outputs=output1) \
              .success(fn=run_name, inputs=output1, outputs=output2) \
              .success(fn=run_req, inputs=output1, outputs=output3)
    with gr.Tab("App scaffolding"):
        gr.Markdown("Under construction!")

software_dev_app.queue().launch() # queue needed for respond time > 60 sec
