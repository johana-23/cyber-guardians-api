from contextlib import asynccontextmanager
import motor.motor_asyncio
from api.config.settings import settings

MONGO_URI = settings.database_url

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client.get_database()
