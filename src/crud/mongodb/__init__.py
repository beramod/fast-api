import datetime
from src.database.mongodb import get_client

class BaseCollection:
    db_type = ''
    database_name = ""
    collection_name = ""

    @classmethod
    def get_database(cls, db_type, database_name):
        return get_client(db_type)[database_name]

    @classmethod
    async def count(cls, query = {}):
        db = cls.get_database(cls.db_type, cls.database_name)
        collection_object = db[cls.collection_name]
        count = await collection_object.count_documents(query)
        return count

    @classmethod
    async def _find_exec(cls, collection_name, query, projection, sort, skip, display_cnt):
        if projection:
            if not projection.get('_id'):
                projection.update({'_id': False})
        else:
            projection = {'_id': False}
        db = cls.get_database(cls.db_type, cls.database_name)
        collection_object = db[collection_name]
        cursor = collection_object.find(query, projection)
        result = []
        cursor.skip(skip)
        if sort is not None:
            cursor.sort(sort[0], sort[1])
        cursor.limit(display_cnt)
        async for document in cursor:
            result.append(document)
        await cursor.close()
        return result

    @classmethod
    async def find(cls, query, projection = {}, sort = None, skip = 0, display_cnt = 999999999):
        result = await cls._find_exec(cls.collection_name, query, projection, sort, skip, display_cnt)
        return result

    @classmethod
    async def find_merge_collection(cls, query, date_at_from, date_at_to, projection = {}, sort = None, skip = 0, display_cnt = 999999999):
        coll_names = cls.make_coll_names(date_at_from, date_at_to)
        result = []
        for coll_name in coll_names:
            result_temp = await cls._find_exec(coll_name, query, projection, sort, skip, display_cnt)
            result.extend(result_temp)
        return result

    @classmethod
    async def count_merge_collection(cls, query, date_at_from, date_at_to):
        coll_names = cls.make_coll_names(date_at_from, date_at_to)
        total_cnt = 0
        for coll_name in coll_names:
            db = cls.get_database(cls.db_type, cls.database_name)
            collection_object = db[coll_name]
            total_cnt += await collection_object.count_documents(query)

        return total_cnt

    @classmethod
    def make_coll_names(cls, date_at_from, date_at_to):
        s_y = int(date_at_from[:2])
        s_m = int(date_at_from[2:4])
        e_y = int(date_at_to[:2])
        e_m = int(date_at_to[2:4])
        coll_names = []
        while True:
            if (s_y > e_y) or (s_y == e_y and s_m > e_m):
                break
            str_y = f'{"0" if s_y < 10 else ""}{str(s_y)}'
            str_m = f'{"0" if s_m < 10 else ""}{str(s_m)}'
            coll_names.append(cls.collection_name + str_y + str_m)
            s_m += 1
            if s_m > 12:
                s_y += 1
                s_m = 1
        return coll_names

    @classmethod
    async def update_one(cls, query, update_doc):
        db = cls.get_database(cls.db_type, cls.database_name)
        collection_object = db[cls.collection_name]
        now = datetime.datetime.now()
        update_doc['updatedAt'] = now
        res = await collection_object.update_one(query, {'$set': update_doc})
        if update_doc.get('_id'):
            update_doc.pop('_id')
        return res

    @classmethod
    async def update_many(cls, query, update_doc):
        db = cls.get_database(cls.db_type, cls.database_name)
        collection_object = db[cls.collection_name]
        now = datetime.datetime.now()
        update_doc['updatedAt'] = now
        res = await collection_object.update_many(query, {'$set': update_doc})
        return res

    @classmethod
    async def get_for_search(cls, query, projection):
        result = await cls.find(query, projection)
        if result:
            return result[0]
        return None

    @classmethod
    async def insert(cls, data, collection_name = None):
        if not collection_name:
            collection_name = cls.collection_name
        db = cls.get_database(cls.db_type, cls.database_name)
        collection_object = db[collection_name]
        now = datetime.datetime.now()
        try:
            if type(data) is list:
                for each in data:
                    each['createdAt'] = now
                    each['updatedAt'] = now
                collection_object.insert_many(data)
            elif type(data) is dict:
                data['createdAt'] = now
                data['updatedAt'] = now
                collection_object.insert_one(data)
            if data.get('_id'):
                data.pop('_id')
            return True
        except Exception:
            return False

    @classmethod
    async def delete(cls, query):
        db = cls.get_database(cls.db_type, cls.database_name)
        collection_object = db[cls.collection_name]
        return await collection_object.delete_many(query)
