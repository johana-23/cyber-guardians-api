from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Game(BaseModel):
    id: str = Field(alias="_id")
    user_id: str
    score: int = Field(default_factory=0)
    character_variation: int
    current_level: int
    levels: list
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
