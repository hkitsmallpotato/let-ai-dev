from llama_cpp import Llama
import gradio as gr

from huggingface_hub import hf_hub_download

import zipfile

from githubkit import GitHub, TokenAuthStrategy

import base64
import json #json.load(file path)

import jsom

# Utility
def b64e(s):
    return base64.b64encode(s.encode()).decode()

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
promptset = [("init", "prompt_initial.md"), ("req", "prompt_requirement.md"), ("name", "prompt_name.md"), ("guide", "prompt_guide.md"), ("guide_refine", "prompt_guide_refine.md"), ("extract", "prompt_extract.md")]
for prompt_key, filename in promptset:
    with open(filename, "r") as f:
        system_prompts[prompt_key] = f.read()


file_generated = ["user_out_init.md", "user_out_name.md", "user_out_req.md"]

def update_asset(download_assets, ses_state, text):
    cur_file_name = file_generated[ses_state]
    with open(cur_file_name, "w") as f:
        f.write(text)
    return (file_generated[:ses_state + 1], ses_state + 1)


# Automatically make a commit to github, return commit url
def make_commit_to_github(account, repo_name, files, commit_msg, gh_strat):
    with GitHub(gh_strat) as github:
        resp = github.rest.repos.get(owner=account, repo=repo_name)
        repo = resp.parsed_data

        resp2 = github.rest.repos.get_branch(owner=account, repo=repo_name, branch=repo.default_branch)
        b2 = resp2.parsed_data
        prev_sha = b2.commit.sha

        graphql_query = """mutation ($input: CreateCommitOnBranchInput!) {
            createCommitOnBranch(input: $input) { commit { url } } }"""

        graphql_var = {
            "input": {
              "branch": {
                "repositoryNameWithOwner": account + "/" + repo_name,
                "branchName": repo.default_branch
              },
              "message": {"headline": commit_msg },
              "fileChanges": {
                "additions": files
              },
              "expectedHeadOid": prev_sha
        }
        }
        commit_result = github.graphql(graphql_query, graphql_var)

        return commit_result["createCommitOnBranch"]["commit"]["url"]


def convert_format_dirty(file_obj, base):
    return { "path": base + "/" + file_obj["name"], "contents": b64e(file_obj["content"]) }

#tester123 = [convert_format_dirty(x, "hello") for x in machine_generated_scaffold]
#TokenAuthStrategy(GITHUB_PAT_SINGLE_REPO)



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


# Prompt chain for the app scaffolding part
def gen_guide(query):
    p = system_prompts["guide"].format(q=query)
    #if is_streaming:
    stream = run_llm_stream(p, 700)
    for current_output in stream:
        yield current_output
    #else:
    #    result = run_llm(p, max_token)
    #    yield result

def gen_agent_commands(generated_guide):
    #p = system_prompts["guide_refine"].format(guide=sample_output_guide)
    p = system_prompts["guide_refine"].format(guide=generated_guide)
    result = run_llm(p, 400)
    print(result)
    return result

def gen_file_list(generated_guide, generated_script):
    p = system_prompts["extract"].format(guide=generated_guide, script=generated_script)
    result = run_llm(p, 800)
    print(result)
    return result

def try_parse_jsom(commands_jsom):
    return jsom.JsomParser(ignore_warnings=jsom.ALL_WARNINGS).loads(commands_jsom)

def commit_to_github(myfiles, gh_org_acc, gh_repo, gh_base_path, gh_pat):
    filelist = []
    if isinstance(myfiles, list):
        filelist = myfiles
    elif isinstance(myfiles, dict):
        if "files" in myfiles.keys():
            filelist = myfiles["files"]
        elif "file" in myfiles.keys():
            filelist = myfiles["file"]
        else:
            raise ValueError("No file nor files attribute")
    else:
        raise ValueError("Not list nor dict")
    gh_fileset = [convert_format_dirty(x, gh_base_path) for x in filelist]
    return make_commit_to_github(gh_org_acc, gh_repo, gh_fileset, "[Test] Auto AI commit", TokenAuthStrategy(gh_pat))



def gen_zipfile(dummy):
    with zipfile.ZipFile("user_out_all.zip", mode="w") as archive:
        for filename in ["user_out_init.md", "user_out_name.md", "user_out_req.md"]:
            archive.write(filename)
    return ["user_out_init.md", "user_out_name.md", "user_out_req.md", "user_out_all.zip"]


# TODO: Also just copied from quickstart doc
copyediting = { "intro": """# Auto Software Dev Demo 
This is a Proof-of-concept for using LLM to automate the SDLC. 

**Important Caveat:**
- *No quality gaurantee, it may fail completely.*
- *Haven't yet audited for privacy (eg console log), don't enter personal/sensitive info.*
- *Ditto for security - for app scaffolding demo please use a PAT locked to an empty repo with no other access if you want to try.*
- *Prompts are still being experimented on - app scaffolding is unreliable, and prompt injection attack is possible.*
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
        with gr.Row():
            with gr.Column(scale=1):
                gh_org_acc = gr.Textbox(label="Org/account")
                gh_repo = gr.Textbox(label="Repo")
                gh_base_path = gr.Textbox(label="Base Path")
                gh_pat = gr.Textbox(label="Personal Access Token")
            with gr.Column(scale=2):
                with gr.Box():
                    with gr.Row():
                        scaffold_query = gr.Textbox(label="Scaffolding Query")
                        ask2_btn = gr.Button("Ask")
                    with gr.Row():
                        ans2 = gr.Textbox(label="Guide")
                gen_btn = gr.Button("Generate app")
                commit_url = gr.Textbox(label="Commit URL")
                extracted_shell_script = gr.State("")
                extracted_files = gr.State("")
                extracted_files_parsed = gr.State()
        ask2_btn.click(fn=gen_guide, inputs=scaffold_query, outputs=ans2)
        gen_btn.click(fn=gen_agent_commands, inputs=ans2, outputs=extracted_shell_script) \
          .success(fn=gen_file_list, inputs=[ans2, extracted_shell_script], outputs=extracted_files) \
          .success(fn=try_parse_jsom, inputs=extracted_files, outputs=extracted_files_parsed) \
          .success(fn=commit_to_github, inputs=[extracted_files_parsed, gh_org_acc, gh_repo, gh_base_path, gh_pat], outputs=commit_url)


software_dev_app.queue().launch() # queue needed for respond time > 60 sec
