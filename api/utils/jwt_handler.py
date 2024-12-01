from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

import jwt
from api.config.settings import settings
from api.models.user import User
from datetime import datetime

oauth2_scheme = HTTPBearer()


def create_access_token(user: User) -> str:
    to_encode = user.model_dump().copy()

    for key, value in to_encode.items():
        if isinstance(value, datetime):
            to_encode[key] = value.isoformat()

    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.jwt_algorithm)

    return encoded_jwt


def verify_access_token(token: str) -> int:
    try:
        payload = jwt.decode(token, settings.secret_key,
                             algorithms=[settings.jwt_algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token")


def get_session_user(authorization: str = Depends(oauth2_scheme)) -> dict:
    token = authorization.credentials
    payload = verify_access_token(token)

    return payload
