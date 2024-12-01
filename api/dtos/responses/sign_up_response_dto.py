from typing import Optional
from pydantic import BaseModel, Field

from api.dtos.responses.get_current_user_response_dto import GetCurrentUserResponseDto


class SignUpResponseDto(BaseModel):
    auth_token: Optional[str] = Field(default=None)
    user: GetCurrentUserResponseDto
