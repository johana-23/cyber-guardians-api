from fastapi import HTTPException, status

from api.dtos.requests.sign_in_request_dto import SignInRequestDto
from api.dtos.responses.sign_in_response_dto import SignInResponseDto
from api.models.user import User
from api.utils.jwt_handler import create_access_token
from api.services.user_service import UserService
from api.utils.security import verify_password

user_service = UserService()


class AuthService:
    async def sign_in(self, user_credentials: SignInRequestDto) -> SignInResponseDto:
        user: User = await user_service.get_user_by_email(user_credentials.email)

        if not user or not verify_password(user_credentials.password, user.password):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                                "Correo electrónico o contraseña incorrectos")

        return {'auth_token': create_access_token(user), 'user': user}

    def _create_access_token(self, user: User) -> str:
        token_data = {"sub": user}
        access_token = create_access_token(data=token_data)

        return access_token
