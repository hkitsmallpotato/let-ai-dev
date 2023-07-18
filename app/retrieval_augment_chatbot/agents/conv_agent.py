class ConversationalAgent:
    def __init__(self, base_prompt, llm_base, llm_code):
        self.base_prompt = base_prompt
        self.context = []
        self.llm_base = llm_base
        self.llm_code = llm_code
        self.thoughts = []
        self.readyToAnswer = False
    
    def _renderConvHistory(self):
        pass
    def _renderThoughts(self):
        pass
    
    def setContext(self, chat_history):
        self.context = chat_history
    def think(self):
        prompt = self.base_prompt.format(input=self._renderConvHistory())
        prompt = prompt + self._renderThoughts()
        prompt = prompt + "\n*Thought {k}*: ".format(k=1)
        raw_response = self.llm_base.generate(prompt, "normal", 300)
        #self.thoughts.append() TODO

        return detectAction(raw_response)
    
    def detectAction(self, raw_response):
        prompt = detect_action_prompt.format(response=raw_response)
        self.llm_code(prompt, "precise", 100)
    
    def appendObservation(self, action_result):
        self.thoughts[-1].addObservation(action_result)
    
    def generate_response(self):
        if not self.readyToAnswer:
            raise Error()
        
    def resetThoughts(self):
        pass
