from src.crud.mongodb.meta import MetaBaseCollection
from src.models.mongodb_document.machines_model import MachineSearch

class MachinesCollection(MetaBaseCollection):
    db_type = 'hot'
    database_name = "meta"
    collection_name = "machines"

    @classmethod
    async def get_machines(cls, mcno = None, host_name = None, projection = None, sort_query = None, skip = 0, display_cnt = 999999999):
        query = {}
        if mcno:
            query["mcno"] = mcno
        if host_name:
            query["hostName"] = host_name

        sort_query = sort_query if sort_query is not None else ["hostName", 1]

        result = await cls.find(query, projection, sort_query, skip, display_cnt)
        return result

    @classmethod
    async def get_machines_by_host_names(cls, host_names: list = None, projection = None, sort_query = None, skip = 0, display_cnt = 999999999):
        query = {}
        if host_names:
            query["hostName"] = {
                "$in" : host_names
            }

        sort_query = sort_query if sort_query is not None else ["hostName", 1]

        result = await cls.find(query, projection, sort_query, skip, display_cnt)
        return result

    @classmethod
    async def get_machines_by_machine_model(cls, machine_model: MachineSearch, skip=0, display_cnt=999999999, projection=None, sort_query=None):
        query = machine_model.makeQueryDict()
        sort_query = sort_query if sort_query is not None else ['hostName', 1]
        result = await cls.find(query, projection, sort_query, skip, display_cnt)
        return result

    @classmethod
    async def get_machine_info_with_query(cls, query, projection, skip, display_cnt, sort_query):
        sort_query = sort_query if sort_query is not None else ['hostName', 1]
        result = await cls.find(query, projection, sort_query, skip, display_cnt)
        return result



