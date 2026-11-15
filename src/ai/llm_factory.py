from pydantic import BaseModel
from langchain_core.messages import BaseMessage
from ai.llm_providers import LLM, Gemini
from config.env import config

class LLMFactory(LLM):
    def __init__(self, provider: str | None = None):
        super().__init__()
        self.provider = (provider or config.PROVIDER or "GEMINI").upper()
    
    def get_provider(self) -> LLM:
        if self.provider == "GEMINI":
            return Gemini()
        raise Exception(f"Invalid Provider Name: {self.provider}")

    def invoke(self, messages: list[BaseMessage], schema: type[BaseModel] | None = None):
        provider_obj = self.get_provider()
        result = provider_obj.invoke(messages, schema)
        return result
