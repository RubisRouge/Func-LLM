from pydantic import BaseModel
from enum import StrEnum
from typing import Any

from .provider import LLMModel
from .image import ImageConfig
from ..message import Message
from .tools import ToolsConfig

class ThinkingLevel(StrEnum):
    NO = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class LLMConfig(BaseModel):
    temperature : float = 0.8
    top_p : float = 0.9
    top_k : int = 40
    max_tokens : int 
    stop : list[str]
    candidates : int
    presence_penalty : float
    frequency_penalty : float
    thinking : ThinkingLevel

class BasiOutputType(StrEnum): 
    TEXT = "text"
    IMAGE = "image"
    HYBRID = "hybrid"

OutputType = BasiOutputType | BaseModel

class GenerationInput(BaseModel):
    model : LLMModel
    image_config : ImageConfig
    conversation : list[Message]
    llm_config : LLMConfig
    tool_config : ToolsConfig
    output_type : OutputType
    system_prompt : str
    stream : bool