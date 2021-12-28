import datetime
from src.crud.mongodb.api_history import ApiHistoryBaseCollection

class NinesApiHistoryCollection(ApiHistoryBaseCollection):
    db_type = 'hot'
    database_name = 'apiHistory'
    collection_name = 'ninesApiHistory_'

    @classmethod
    async def get_api_history(cls, datetime_from, datetime_to, method = None, uri = None, access_key = None, access_category = None, projection = {}):
        query = {
            'datetimeAt': {
                '$gte': datetime_from,
                '$lte': datetime_to
            }
        }
        if method is not None:
            query['method'] = method
        if uri is not None:
            query['uri'] = uri
        if access_key is not None:
            query['accessKey'] = access_key
        if access_category is not None:
            query['accessCategory'] = access_category
        return await cls.find_merge_collection(query, datetime_from, datetime_to, projection=projection)

    @classmethod
    async def insert_api_history(cls, api_history_doc):
        collection_name = cls.collection_name + datetime.datetime.now().strftime('%y%m')
        return await cls.insert(api_history_doc, collection_name)
