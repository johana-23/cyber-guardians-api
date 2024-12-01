from typing import Any, Optional

from bson import ObjectId

from api.config.database import database
from api.dtos.requests.sign_up_request_dto import SignUpRequestDto
from api.dtos.requests.update_user_request_dto import UpdateUserRequestDto
from api.dtos.responses.sign_up_response_dto import SignUpResponseDto
from api.models.user import User
from datetime import datetime, timezone


class UserRepository:
    async def add_user(self, user_data: SignUpRequestDto) -> SignUpResponseDto:
        user_document: dict[str, Any] = user_data.model_dump()
        user_document['created_at'] = datetime.now(timezone.utc)

        created_user: User = await database.users.insert_one(user_document)
        user_document["id"] = str(created_user.inserted_id)

        return user_document

    async def get_user_by_email(self, user_email: str) -> Optional[User]:
        user_document = await database.users.find_one({"email": user_email})

        if user_document:
            user_document["_id"] = str(user_document["_id"])
            return User(**user_document)

        return None

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        object_id = ObjectId(user_id)
        user_document = await database.users.find_one({"_id": object_id})

        if user_document:
            user_document["_id"] = str(user_document["_id"])
            return User(**user_document)

        return None

    async def delete_user_by_email(self, user_email: str) -> bool:
        result = await database.users.delete_one({"email": user_email})
        return result.deleted_count > 0

    async def update_user(self, user_id: str, user_data: UpdateUserRequestDto) -> User:
        object_id = ObjectId(user_id)
        user_data['updated_at'] = datetime.now(timezone.utc)
        result = await database.users.update_one({"_id": object_id}, [{"$set": user_data}])

        return result.modified_count > 0
