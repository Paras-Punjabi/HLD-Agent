from dotenv import load_dotenv
from dataclasses import dataclass
import os

load_dotenv()

@dataclass(frozen=True)
class EnvConfig:
    DB_URL = os.getenv("DB_URL")

config = EnvConfig()
