from pydantic import BaseModel, EmailStr


class SignInRequestDto(BaseModel):
    email: EmailStr
    password: str
