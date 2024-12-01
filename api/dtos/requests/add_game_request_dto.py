from typing import Optional
from pydantic import BaseModel


class AddGameRequestDto(BaseModel):
    score: int
    character_variation: int
    current_level: int
    levels: Optional[list]
