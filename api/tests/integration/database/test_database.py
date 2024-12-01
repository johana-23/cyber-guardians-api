import pytest
from motor.motor_asyncio import AsyncIOMotorClient
from api.config.settings import settings


@pytest.mark.asyncio
async def test_mongodb_connection():
    client = AsyncIOMotorClient(settings.database_url)
    try:
        await client.admin.command("ping")
        assert True, "Successfully connected to MongoDB"
    except Exception as e:
        assert False, f"Failed to connect to MongoDB: {e}"
    finally:
        client.close()
