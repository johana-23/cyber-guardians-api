from pydantic import BaseModel

from api.dtos.responses.get_current_user_response_dto import GetCurrentUserResponseDto


class SignInResponseDto(BaseModel):
    auth_token: str
    user: GetCurrentUserResponseDto
