from typing import Any, List, Mapping, Optional

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

from gradio_client import Client

import time

class CustomLLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "custom"
    
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        c = Client("https://openaccess-ai-collective-manticore-13b-chat-pyg.hf.space/")
        job = c.submit(prompt, api_name="/predict")
        while not job.done():
            print(job.status())
            time.sleep(5)
        return job.outputs()[-1]
    
    #@property
    #def _identifying_params(self) -> Mapping[str, Any]:
    #    """Get the identifying parameters."""
    #    return {"n": self.n}

