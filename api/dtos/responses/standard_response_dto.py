from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")


class StandardResponseDto(BaseModel, Generic[T]):
    status_code: int
    status: str
    message: Optional[str] = None
    data: Optional[T] = None

    class Config:
        # Exclude fields with None values from the serialized output
        exclude_none = True
