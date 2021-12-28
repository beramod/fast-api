from src.api.yggnet import YggnetBaseController
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from .services import YggnetHandler
from src.models.mongodb_document.yggnet_device import YggnetDevice
from src.models.mongodb_document.yggnet_status import YggnetStatus
from typing import Union
yggnet_v1_router = InferringRouter()

@cbv(yggnet_v1_router)
class YggnetController(YggnetBaseController):
    @yggnet_v1_router.get('/device/paging')
    async def get_yggnet_device_list(self, search_query: str = None, page: int = 1, display_cnt: int = 50,
                                     sort_category: str = 'uid', sort_order: int = -1):
        response = await YggnetHandler.get_yggnet_device_list(search_query, page, display_cnt, sort_category, sort_order)
        return {'result': response, 'message': '', 'code': 200}

    @yggnet_v1_router.post('/device/lorygate')
    async def insert_lory_gate(self, serial_number, location_x, location_y, memo = ""):
        response = await YggnetHandler.insert_lory_gate(serial_number, memo, location_x, location_y)
        return {'result': response, 'message': '', 'code': 200}

    @yggnet_v1_router.post('/device/loryclient')
    async def insert_lory_client(self, serial_number: str, mcno: int, memo: str = ""):
        response = await YggnetHandler.insert_lory_client(serial_number, mcno, memo)
        return {'result': response, 'message': '', 'code': 200}

    @yggnet_v1_router.put('/device/{uid}')
    async def update_yggnet_device(self, uid, update_yggnet_device_object: YggnetDevice):
        success, result = await YggnetHandler.update_yggnet_device(uid, update_yggnet_device_object)
        if not success:
            return {'result': {'success': False}, 'message': success, 'code': 400}
        return {'result': {'success': True, 'document': result}, 'message': "", 'code': 200}

    @yggnet_v1_router.delete('/device')
    async def delete_yggnet_device(self, uid):
        success, result = await YggnetHandler.delete_yggnet_device(uid)
        if not success:
            return {'result': {'success': False}, 'message': success, 'code': 400}
        return {'result': {'success': True, 'document': result}, 'message': "", 'code': 200}

    @yggnet_v1_router.get('/status')
    async def get_yggnet_status(self, uid=None):
        response = await YggnetHandler.get_yggnet_status(uid)
        return {'result': response, 'message': '', 'code': 200}

    @yggnet_v1_router.put('/status')
    async def update_yggnet_status(self, yggnet_status_object: YggnetStatus):
        response = await YggnetHandler.upsert_yggnet_status(yggnet_status_object)
        return {'result': response, 'message': '', 'code': 200}

    @yggnet_v1_router.get('/device/filter')
    async def get_filtered_device(self, field: str = None, value: Union[str, int] = None,\
                                        page: int = None, display_cnt: int = None):
        response = await YggnetHandler.get_filtered_device(field, value, page, display_cnt)
        return {'result': response, 'message': '', 'code': 200}