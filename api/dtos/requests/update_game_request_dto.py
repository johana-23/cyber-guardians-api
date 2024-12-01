from typing import Optional
from pydantic import BaseModel, Field


class UpdateGameRequestDto(BaseModel):
    score: Optional[int] = Field(default=None)
    character_variation: Optional[int] = Field(default=None)
    current_level: Optional[int] = Field(default=None)
    levels: Optional[list] = Field(default=None)
