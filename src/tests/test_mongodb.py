import pytest
import pymongo.errors
from motor.motor_asyncio import AsyncIOMotorClient

@pytest.fixture(scope="module")
async def mongodb_client():
    client = AsyncIOMotorClient(
        'localhost:12000',
        serverSelectionTimeoutMS=100,
        uuidRepresntation="standard",        
    )
    
    try:
        info = await client.server_info()
        print(info)
        yield client
        client.close()
    except pymongo.errors.ServerSelectionTimeoutError:
        pytest.skip("MongoDB not available", allow_module_level=True)
        return
    
