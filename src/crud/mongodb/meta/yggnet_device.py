from src.crud.mongodb.meta import MetaBaseCollection
from src.models.mongodb_document.yggnet_device import YggnetDevice

class YggnetDeviceCollection(MetaBaseCollection):
    db_type = 'hot'
    database_name = "meta"
    collection_name = "yggnetDevice"

    @classmethod
    async def get_yggnet_device(cls, uid: str = None, device_type: str = None, mcno: int = None, device_id: str = None,
                                serial_number: str = None, memo: str = None):
        query = {}

        if uid:
            query["uid"] = uid
        if device_type:
            query["deviceType"] = device_type
        if mcno:
            query["mcno"] = mcno
        if device_id:
            query["deviceId"] = device_id
        if serial_number:
            query["serialNumber"] = serial_number
        if memo:
            query["memo"] = {'$regex': memo}

        docs = await cls.find(query)
        result = []
        for obj in docs:
            result.append(YggnetDevice.from_mongo(obj))
        return result

    @classmethod
    async def get_yggnet_device_with_query(cls, query, skip=0, display_cnt=999999999, projection=None, sort_query=None):
        sort_query = sort_query if sort_query is not None else ['uid', 1]
        docs = await cls.find(query, projection, sort_query, skip, display_cnt)
        result = []
        for obj in docs:
            result.append(YggnetDevice.from_mongo(obj))
        return result

    @classmethod
    async def insert_yggnet_device(cls, yggnet_device_object: YggnetDevice):
        document = yggnet_device_object.mongo()
        await cls.insert(document, cls.collection_name)
        if document.get('_id'):
            document.pop('_id')
        return document

    @classmethod
    async def update_yggnet_device(cls, uid, update_yggnet_device_object: YggnetDevice):
        update_doc = update_yggnet_device_object.mongo()
        if update_doc.get('deviceType'):
            update_doc.pop('deviceType')
        if update_doc.get('serialNumber'):
            update_doc.pop('serialNumber')
        return await cls.update_one({'uid': uid}, update_doc)

    @classmethod
    async def delete_yggnet_device(cls, uid):
        query = {'uid': uid}
        return await cls.delete(query)

    @classmethod
    async def get_count(cls, query={}):
        count = await cls.count(query)
        return count