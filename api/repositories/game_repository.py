from typing import Any, List

from bson import ObjectId
from api.config.database import database
from api.dtos.requests.add_game_request_dto import AddGameRequestDto
from api.dtos.requests.update_game_request_dto import UpdateGameRequestDto
from api.dtos.responses.add_game_response_dto import AddGameResponseDto
from datetime import datetime, timezone
from api.dtos.responses.get_game_response_dto import GetGameResponseDto


class GameRepository:
    async def get_games(self, user_id: str) -> List[GetGameResponseDto]:
        games_cursor = database.games.find({"user_id": user_id})
        games_list = await games_cursor.to_list(length=None)

        for game in games_list:
            game["id"] = str(game.pop("_id", None))

        return games_list

    async def get_game(self, game_id: str, user_id: str) -> GetGameResponseDto:
        object_id = ObjectId(game_id)
        game_document = await database.games.find_one({"_id": object_id, "user_id": user_id})
        game_document["id"] = str(game_document['_id'])

        return game_document

    async def add_game(self, game_data: AddGameRequestDto, user_id: int) -> AddGameResponseDto:
        game_document: dict[str, Any] = game_data.model_dump()
        game_document.update({
            "user_id": user_id,
            "created_at": datetime.now(timezone.utc)
        })

        created_game = await database.games.insert_one(game_document)
        game_document["id"] = str(created_game.inserted_id)

        return game_document

    async def update_game(self, game_id, game_data: UpdateGameRequestDto) -> bool:
        object_id = ObjectId(game_id)
        game_data['updated_at'] = datetime.now(timezone.utc)
        result = await database.games.update_one({"_id": object_id}, [{"$set": game_data}])

        return result.modified_count > 0

    async def delete_game(self, game_id: str) -> bool:
        object_id = ObjectId(game_id)
        result = await database.games.delete_one({"_id": object_id})

        return result.deleted_count > 0
