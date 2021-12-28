from src.api.machine import MachineBaseHandler
from src.crud.mongodb.meta.machines import MachinesCollection


class MachineHandler(MachineBaseHandler):
    @classmethod
    async def get_machine_conn_info(cls, mcno: int = None, host_name: str = None):
        machines = await MachinesCollection.get_machines(mcno, host_name)
        for each in machines:
            ssh_shell = None
            if each.get('connectionInfo'):
                conn_info = each.get('connectionInfo')
                ssh_shell = f'ssh -p {conn_info.get("ssh")} {conn_info.get("user")}@{conn_info.get("ip")}'
            each['sshShell'] = ssh_shell
        return machines

    @classmethod
    async def get_machine_info(cls, mcno: str = None, hostName: str = None):
        machines_docs = await MachinesCollection.get_machines(mcno, hostName)
        return machines_docs

    @classmethod
    async def get_machine_info_auto_complete(cls, search_query: str=None, page: int=1, display_cnt: int=10, field: str=None):
        query = {}
        if field:
            query[field] = {"$regex": search_query}
        else:
            queries = []
            queries.append({'hostName': {'$regex': search_query}})
            queries.append({'serverName': {'$regex': search_query}})
            query["$or"] = queries

        projection = {"hostName": 1, "serverName": 1}
        skip = (1 - page) * display_cnt
        result = await MachinesCollection.get_machine_info_with_query(query, projection, skip, display_cnt, None)
        return result

