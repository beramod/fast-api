from src.crud.mongodb.meta import MetaBaseCollection

class PowerStationsCollection(MetaBaseCollection):
    db_type = 'hot'
    database_name = "meta"
    collection_name = "powerStations"

    @classmethod
    async def get_power_station(cls, mcno = None, projection={}):
        query = {}
        sortQuery = ['mcno', 1]
        if mcno:
            query['mcno'] = mcno
        result = await cls.find(query, projection, sortQuery, 0, 1)
        return result

    @classmethod
    async def get_power_stations(cls, mcnos = None, skip=0, display_cnt=999999999, projection=None, sort=None):
        query = {}
        sortQuery = ['mcno', 1]
        if sort:
            sortQuery = sort
        if mcnos:
            query['mcno'] = {'$in': mcnos}
        result = await cls.find(query, projection, sortQuery, skip, display_cnt)
        return result

    @classmethod
    async def get_area_power_stations(cls, area, skip=0, display_cnt=999999999, projection=None, sort_query=None, is_operating=False):
        query = {}
        sort_query = sort_query if sort_query is not None else ['mcno', 1]
        if area is not None and area != "0":
            query["psAddress.area"] = area
        if is_operating:
            query['psStatusCode'] = {'$in': [2,3,4]}

        result = await cls.find(query, projection, sort_query, skip, display_cnt)
        return result

    @classmethod
    async def get_power_stations_with_query(cls, query, skip=0, display_cnt=999999999, projection=None, sort_query=None):
        sort_query = sort_query if sort_query is not None else ['mcno', 1]
        result = await cls.find(query, projection, sort_query, skip, display_cnt)
        return result

    @classmethod
    async def get_count(cls, query={}):
        count = await cls.count(query)
        return count



