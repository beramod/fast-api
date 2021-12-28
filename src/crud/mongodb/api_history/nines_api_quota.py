import datetime
from src.crud.mongodb.api_history import ApiHistoryBaseCollection

class NinesApiQuotaCollection(ApiHistoryBaseCollection):
    db_type = 'hot'
    database_name = 'apiHistory'
    collection_name = 'ninesApiQuota'

    @classmethod
    async def get_api_request_cnt(cls, method, uri, a_key, start_time):
        query = {
            'method': method,
            'uri': uri,
            'aKey': a_key,
            'createdAt': {
                '$gte': start_time
            }
        }
        return await cls.count(query)

    @classmethod
    async def insert_api_request(cls, method, uri, a_key, response_status, process_time):
        expire_time = (datetime.datetime.now() - datetime.timedelta(hours=9)) + datetime.timedelta(minutes=10)
        doc = {
            'method': method,
            'uri': uri,
            'aKey': a_key,
            'status': response_status,
            'processTime': process_time,
            'expireTime': expire_time
        }
        return await cls.insert(doc)
