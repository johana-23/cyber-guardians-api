from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api.controllers.auth_controller import auth_router
from api.controllers.user_controller import users_router
from api.controllers.game_controller import games_router

from api.config.settings import settings
from api.utils.error_handler import http_exception_handler, general_exception_handler

api = FastAPI(title=settings.app_name)

api.add_exception_handler(HTTPException, http_exception_handler)
api.add_exception_handler(Exception, general_exception_handler)


api.include_router(auth_router, prefix='/auth', tags=['Autenticación'])
api.include_router(users_router, prefix='/users', tags=['Usuarios'])
api.include_router(games_router, prefix='/games', tags=['Partidas'])

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
