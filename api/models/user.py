from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class User(BaseModel):
    id: str = Field(alias="_id")
    user_name: str
    email: EmailStr
    password: str
    birth_date: datetime
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
