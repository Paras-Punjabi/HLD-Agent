from abc import ABC, abstractmethod
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage
from pydantic import BaseModel
from config.env import config
import os

class LLM(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def invoke(self, messages: list[BaseMessage], schema: type[BaseModel] | None = None):
        pass

class Gemini(LLM):
    def __init__(self):
        super().__init__()
        model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0,
            api_key=config.GOOGLE_API_KEY
        )
    
    def invoke(self, messages: list[BaseMessage], schema: type[BaseModel] | None = None):
        llm = self.llm
        if schema:
            llm = llm.with_structured_output(schema)
        result = llm.invoke(messages)
        return result
