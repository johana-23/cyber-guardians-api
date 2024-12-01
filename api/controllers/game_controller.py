from fastapi import APIRouter, Depends, status

from api.dtos.requests.add_game_request_dto import AddGameRequestDto
from api.dtos.requests.update_game_request_dto import UpdateGameRequestDto
from api.dtos.responses.add_game_response_dto import AddGameResponseDto
from api.dtos.responses.get_current_user_response_dto import GetCurrentUserResponseDto
from api.dtos.responses.get_game_response_dto import GetGameResponseDto
from api.dtos.responses.standard_response_dto import StandardResponseDto
from api.services.game_service import GameService
from api.utils.jwt_handler import get_session_user


games_router = APIRouter()
game_service = GameService()


@games_router.get('', summary='Obtener partidas del jugador')
async def get_games(current_user: GetCurrentUserResponseDto = Depends(get_session_user)) -> StandardResponseDto[list[GetGameResponseDto]]:
    response = await game_service.get_games(current_user['id'])

    return StandardResponseDto(status_code=status.HTTP_200_OK,
                               status='success',
                               message='Partidas obtenidas',
                               data=response)


@games_router.get('/{game_id}', summary='Obtener partida')
async def get_game(game_id: str, current_user: GetCurrentUserResponseDto = Depends(get_session_user)) -> StandardResponseDto[GetGameResponseDto]:
    response = await game_service.get_game(game_id, current_user['id'])

    return StandardResponseDto(status_code=status.HTTP_200_OK,
                               status='success',
                               message='Partida obtenida',
                               data=response)


@games_router.post('', summary='Crear partida')
async def add_game(game_data: AddGameRequestDto,
                   current_user: GetCurrentUserResponseDto =
                   Depends(get_session_user)) -> StandardResponseDto[AddGameResponseDto]:
    response = await game_service.add_game(game_data, current_user['id'])

    return StandardResponseDto(status_code=status.HTTP_201_CREATED,
                               status='success',
                               message='Partida creada',
                               data=response)


@games_router.put('/{game_id}', summary='Actualizar partida')
async def update_game(game_id: str, game_data: UpdateGameRequestDto, current_user: GetCurrentUserResponseDto =
                      Depends(get_session_user)) -> StandardResponseDto[GetGameResponseDto]:
    await game_service.update_game(game_id, game_data, current_user['id'])

    response = await game_service.get_game(game_id, current_user['id'])

    return StandardResponseDto(status_code=status.HTTP_200_OK,
                               status='success',
                               message='Partida actualizada',
                               data=response)


@games_router.delete('/{game_id}', summary='Eliminar partida')
async def delete_game(game_id: str, current_user: GetCurrentUserResponseDto =
                      Depends(get_session_user)) -> StandardResponseDto[None]:
    await game_service.delete_game(game_id, current_user['id'])

    return StandardResponseDto(status_code=status.HTTP_200_OK,
                               status='success',
                               message='Partida eliminada')
