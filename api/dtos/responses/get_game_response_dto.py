from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class GetGameResponseDto(BaseModel):
    id: str
    user_id: str
    score: int
    character_variation: int
    current_level: int
    levels: list
    created_at: datetime
    updated_at: Optional[datetime] = Field(default=None)
