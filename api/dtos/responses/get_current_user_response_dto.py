from pydantic import BaseModel, EmailStr
from datetime import datetime


class GetCurrentUserResponseDto(BaseModel):
    id: str
    user_name: str
    email: EmailStr
    birth_date: datetime
