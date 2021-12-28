from src.crud.mongodb.meta import MetaBaseCollection

class CodesCollection(MetaBaseCollection):
    db_type = 'hot'
    database_name = "meta"
    collection_name = "codes"

    @classmethod
    async def get_codes(cls, code_group, projection={}, sort_query=None, skip=0, display_cnt=99999):
        query = {}
        if code_group:
            query['codeGroup'] = code_group
        if code_group == 'area':
            query.update({'code': {'$ne': '-'}})

        sort_query = sort_query if sort_query is not None else ['codeGroup', 1]

        result = await cls.find(query, projection, sort_query, skip, display_cnt)
        return result
