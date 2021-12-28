from datetime import datetime
import hashlib, os
from src.api.session import SessionBaseHandler
from src.crud.mongodb.session.nines_api_access_key import NinesApiAccessKeyCollection

class SessionHandler(SessionBaseHandler):
    @classmethod
    async def get_nines_access_key(cls, api_key: str):
        access_key_obj = await NinesApiAccessKeyCollection.get_api_access_key(api_key)
        return access_key_obj

    @classmethod
    async def create_nines_access_key(cls, referer: str, expire_time: datetime, created_user: str):
        api_key = hashlib.sha256(os.urandom(32)).hexdigest()
        generate_key_time = datetime.now().strftime('%y%m%d%H%M')
        doc = {
            'referer': referer,
            'apiKey': api_key,
            'createdUserId': created_user,
            'generateKeyTime': generate_key_time,
            'expireTime': expire_time
        }
        res = await NinesApiAccessKeyCollection.insert_api_access_key(doc)
        if doc.get('_id'):
            doc.pop('_id')
        if res:
            return doc
        return False

    @classmethod
    async def delete_nines_api_key(cls, api_key: str):
        res = await NinesApiAccessKeyCollection.delete_api_access_key(api_key)
        return True