from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UpdateUserRequestDto(BaseModel):
    user_name: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    email: Optional[EmailStr] = Field(default=None)
    birth_date: Optional[datetime] = Field(default=None)
