import datetime
from src.crud.mongodb.yggnet import YggnetBaseCollection
from src.models.mongodb_document.yggnet_status import YggnetStatus

class YggnetStatusCollection(YggnetBaseCollection):
    db_type = 'hot'
    database_name = "yggnet"
    collection_name = "yggnetStatus"

    @classmethod
    async def get_yggnet_status(cls, uid: str = None):
        query = {}
        if uid:
            query["uid"] = uid
        docs = await cls.find(query)
        result = []
        for obj in docs:
            result.append(YggnetStatus.from_mongo(obj))
        return result

    @classmethod
    async def upsert_yggnet_status(cls, yggnet_status_object: YggnetStatus):
        query = {'uid': yggnet_status_object.uid}
        cnt = await cls.count(query)
        now = datetime.datetime.now()
        if cnt == 0:
            yggnet_status_object.createdAt = now
            yggnet_status_object.updatedAt = now
            return await cls.insert(yggnet_status_object.mongo(), cls.collection_name)
        else:
            yggnet_status_object.updatedAt = now
            doc = await cls.update_one(query, yggnet_status_object.mongo())
            return True
