from src.crud.mongodb.meta.power_stations import PowerStationsCollection

class MetaDataUtil:
    @classmethod
    def make_map(cls, data, key):
        result_map = {}
        for each in data:
            result_map[each.get(key)] = each
        return result_map

    @classmethod
    async def get_ps_map(cls, mcnos, projection):
        ps_list = await PowerStationsCollection.get_power_stations(mcnos = mcnos, projection = projection)
        ps_map = cls.make_map(ps_list, 'mcno')
        return ps_map