from fastapi import APIRouter, status

from api.dtos.requests.sign_in_request_dto import SignInRequestDto
from api.dtos.responses.sign_in_response_dto import SignInResponseDto
from api.dtos.responses.sign_up_response_dto import SignUpResponseDto
from api.dtos.responses.standard_response_dto import StandardResponseDto
from api.services.auth_service import AuthService
from api.services.user_service import UserService
from api.dtos.requests.sign_up_request_dto import SignUpRequestDto

auth_router = APIRouter()
auth_service = AuthService()
user_service = UserService()


@auth_router.post('/sign-up', summary="Registro de usuarios")
async def sign_up(user_data: SignUpRequestDto) -> StandardResponseDto[SignUpResponseDto]:
    response = await user_service.add_user(user_data)
    sign_in_request = await sign_in(user_data)

    user = response['user']['user_name']
    response['auth_token'] = sign_in_request.data['auth_token']

    return StandardResponseDto(status_code=status.HTTP_201_CREATED,
                               status='success',
                               message=f'{user} registrado(a) exitosamente',
                               data=response)


@auth_router.post('/sign-in', summary='Inicio de sesión')
async def sign_in(user_credentials: SignInRequestDto) -> StandardResponseDto[SignInResponseDto]:
    response = await auth_service.sign_in(user_credentials)
    user = response['user']

    return StandardResponseDto(status_code=status.HTTP_200_OK,
                               status='success',
                               message=f'Bienvenido(a) {user.user_name}',
                               data=response)
