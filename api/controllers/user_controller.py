from fastapi import APIRouter, Depends, status

from api.dtos.requests.update_user_request_dto import UpdateUserRequestDto
from api.dtos.responses.get_current_user_response_dto import GetCurrentUserResponseDto
from api.dtos.responses.standard_response_dto import StandardResponseDto
from api.services.user_service import UserService
from api.utils.jwt_handler import get_session_user


users_router = APIRouter()
user_service = UserService()


@users_router.get('/me', summary='Obtener datos del usuario en sesión')
async def get_current_user(current_user: GetCurrentUserResponseDto
                           = Depends(get_session_user)) -> StandardResponseDto[GetCurrentUserResponseDto]:
    response = await user_service.get_user_by_id(current_user['id'])

    return StandardResponseDto(status_code=status.HTTP_200_OK,
                               status='success',
                               message='Usuario autenticado',
                               data=response)


@users_router.put('', summary='Actualizar usuario')
async def update_user(user_data: UpdateUserRequestDto, current_user: GetCurrentUserResponseDto
                      = Depends(get_session_user)) -> StandardResponseDto[GetCurrentUserResponseDto]:
    await user_service.update_user(current_user, user_data)

    return StandardResponseDto(status_code=status.HTTP_200_OK,
                               status='success',
                               message='Usuario actualizado')


@users_router.delete('/{email}', summary='Eliminar usuario')
async def delete_user(email: str) -> StandardResponseDto:
    await user_service.delete_user_by_email(email)

    return StandardResponseDto(status_code=status.HTTP_200_OK,
                               status='success',
                               message=f'Usuario {email} eliminado')
