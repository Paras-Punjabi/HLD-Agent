from dotenv import load_dotenv
from dataclasses import dataclass
import os

load_dotenv()

@dataclass(frozen=True)
class EnvConfig:
    DB_URL: str = os.getenv("DB_URL", "sqlite:///./hld_agent.db")
    GOOGLE_API_KEY: str | None = os.getenv("GOOGLE_API_KEY")
    PROVIDER: str = os.getenv("PROVIDER", "GEMINI")

config = EnvConfig()
