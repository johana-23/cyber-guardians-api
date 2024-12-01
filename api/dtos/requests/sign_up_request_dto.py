from pydantic import BaseModel, EmailStr
from datetime import datetime


class SignUpRequestDto(BaseModel):
    user_name: str
    password: str
    email: EmailStr
    birth_date: datetime
