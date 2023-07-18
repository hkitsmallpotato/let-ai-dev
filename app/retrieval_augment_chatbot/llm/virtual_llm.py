import modal

class VirtualLLM:
    def __init__(self, deployment_name, method_name):
        self.deployment_name = deployment_name
        self.method_name = method_name
        self.llm = modal.Function.lookup(deployment_name, method_name)
    
    def generate(self, prompt, config, max_toks):
        if config == "precise":
            temp = 0.2
            top_p = 0.95
            tok_k = 50
            result = self.llm.call(prompt, temp, top_p, top_k, max_toks)
        else:
            temp = 0.7
            top_p = 0.95
            top_k = 100
            rep_pen = 1.1
            result = self.llm.call(prompt, temp, top_p, top_k, rep_pen, max_toks)
        print(result)
        return result
