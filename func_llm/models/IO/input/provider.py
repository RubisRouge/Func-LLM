from pydantic import BaseModel
from enum import StrEnum
from typing import Any

class Provider(StrEnum):
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"
    MISTRAL = "mistral"
    OPENAI = "openai"

class Region(StrEnum) :
    EUW1 = "europe-west1" 

class LLMModel(BaseModel):
    name : str
    id : str
    provider : Provider
    endpoint : str
    region : Region