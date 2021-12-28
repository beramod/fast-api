from src.api.machine import MachineBaseController
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from src.api.machine.services import MachineHandler

machine_v1_router = InferringRouter()


@cbv(machine_v1_router)
class MachineController(MachineBaseController):
    @machine_v1_router.get("/conn-info/", tags=["conn-info"])
    @machine_v1_router.get("/conn-info/{host_name}", tags=["conn-info"])
    async def get_machine_conn_info(self, mcno: int = None, host_name: str = None):
        response = await MachineHandler.get_machine_conn_info(mcno, host_name)
        return {"result": response, 'message': '', 'code': 200}

    @machine_v1_router.get("/", tags=["machine-info"])
    @machine_v1_router.get("/{host_name}", tags=["machine-info"])
    async def get_machine_info(self, mcno: int = None, host_name: str = None):
        response = await MachineHandler.get_machine_info(mcno, host_name)
        return {"result": response, 'message': '', 'code': 200}

    @machine_v1_router.get("/auto-complete/{search_query}", tags=["machine-info", "auto-complete"])
    async def get_machine_info_auto_complete(self, search_query: str = None, page: int = 1, display_cnt: int = 15,
                                             field: str = None):
        response = await MachineHandler.get_machine_info_auto_complete(search_query, page, display_cnt, field)
        return {"result": response, 'message': '', 'code': 200}
