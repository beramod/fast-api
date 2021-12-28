from typing import List
from src.crud.mongodb.session import SessionBaseCollection
from src.models.mongodb_document.nines_api_access_key_model import NinesApiAccessKey

class NinesApiAccessKeyCollection(SessionBaseCollection):
    db_type = 'hot'
    database_name = 'session'
    collection_name = 'ninesApiAccessKey'

    @classmethod
    async def get_api_access_key(cls, api_key) -> List[NinesApiAccessKey]:
        query = {}
        if api_key is not None:
            query['apiKey'] = api_key
        response =  await cls.find(query)
        result = []
        for each in response:
            result.append(NinesApiAccessKey.from_mongo(each))
        return result

    @classmethod
    async def insert_api_access_key(cls, nines_api_access_key_doc):
        return await cls.insert(nines_api_access_key_doc)

    @classmethod
    async def delete_api_access_key(cls, api_key):
        return await cls.delete({'apiKey': api_key})