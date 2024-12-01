from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class AddGameResponseDto(BaseModel):
    id: str
    user_id: str
    score: int
    character_variation: int
    current_level: int
    levels: Optional[list]
    created_at: datetime
