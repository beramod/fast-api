from typing import List, Union
from src.api.yggnet import YggnetBaseHandler
from src.crud.mongodb.meta.yggnet_device import YggnetDeviceCollection
from src.crud.mongodb.meta.power_stations import PowerStationsCollection
from src.crud.mongodb.yggnet.yggnet_status import YggnetStatusCollection
from src.models.mongodb_document.yggnet_device import YggnetDevice
from src.models.mongodb_document.yggnet_status import YggnetStatus
from src.models.mongodb_document.location import Location

class YggnetHandler(YggnetBaseHandler):
    @classmethod
    def _type_check(cls, search_query):
        try:
            val = int(search_query)
            return 'int'
        except Exception:
            return 'str'

    @classmethod
    async def get_yggnet_device_list(cls, search_query: str, page: int = 1, display_cnt: int = 50,
                                         sort_category: str = 'uid', sort_order: int = -1):
        query = {}
        if search_query:
            docs = await PowerStationsCollection.get_power_stations_with_query(\
                {'psName': {'$regex': search_query}}, projection={'mcno': True})
            mcnos = list(map(lambda el: el.get('mcno'), docs))
            or_query = [
                {'serial_number': {'$regex': search_query}},
                {'uid': {'$regex': search_query}},
                {'device_id': {'$regex': search_query}},
                {'$expr': {'$regexMatch': {'input': {'$toString': '$mcno'}, 'regex': '.*' + search_query + '.*'}}},
            ]

            if len(mcnos) > 0:
                or_query.append({'mcno': {'$in': mcnos}})
            query = {'$or': or_query}

        total_doc_cnt = await YggnetDeviceCollection.count(query)
        sort_query = [sort_category, sort_order]

        docs = await YggnetDeviceCollection.get_yggnet_device_with_query(\
                query, (page - 1) * display_cnt, display_cnt, None, sort_query)

        res = {
            'docs': docs,
            'totalDocCnt': total_doc_cnt,
            'curPage': page,
        }
        return res

    @classmethod
    async def insert_lory_gate(cls, serial_number, memo, location_x, location_y):
        yggnet_devices = await YggnetDeviceCollection.get_yggnet_device(device_type="1")
        device_id = None
        if len(yggnet_devices) == 0:
            device_id = '00001'
        else:
            yggnet_devices.sort(key=lambda el: int(el.device_id), reverse=True)
            latest_object: YggnetDevice = yggnet_devices[0]
            device_id = str(int(latest_object.device_id) + 1)
            while len(device_id) != 5:
                device_id = '0' + device_id

        location: Location = Location()
        location.type = 'Point'
        location.coordinates = [location_x, location_y]
        yggnet_device_object: YggnetDevice = YggnetDevice()
        yggnet_device_object.location = location
        yggnet_device_object.device_id = device_id
        yggnet_device_object.device_type = "1"
        yggnet_device_object.serial_number = serial_number
        yggnet_device_object.memo = memo
        yggnet_device_object.uid = "1" + device_id

        result = await YggnetDeviceCollection.insert_yggnet_device(yggnet_device_object)
        return yggnet_device_object.mongo()

    @classmethod
    async def insert_lory_client(cls, serial_number, mcno, memo):
        power_stations = await PowerStationsCollection.get_power_station(mcno, {'mcno': True, 'location': True})
        if len(power_stations) < 1:
            return False, "not exsist mcno"
        power_station = power_stations[0]
        yggnet_devices: List[YggnetDevice] = await YggnetDeviceCollection.get_yggnet_device(mcno=mcno, device_type="2")
        device_id = None
        if len(yggnet_devices) == 0:
            device_id = '001'
        else:
            yggnet_devices.sort(key=lambda el: int(el.device_id), reverse=True)
            latest_object: YggnetDevice = yggnet_devices[0]
            device_id = str(int(latest_object.device_id) + 1)
            while len(device_id) != 3:
                device_id = '0' + device_id

        location: Location = Location()
        location.type = 'Point'
        location.coordinates = power_station.get('location').get('coordinates')
        yggnet_device_object: YggnetDevice = YggnetDevice()
        yggnet_device_object.location = location
        yggnet_device_object.mcno = mcno
        yggnet_device_object.device_id = device_id
        yggnet_device_object.device_type = "2"
        yggnet_device_object.serial_number = serial_number
        yggnet_device_object.memo = memo
        yggnet_device_object.uid = "2" + device_id + str(mcno)

        result = await YggnetDeviceCollection.insert_yggnet_device(yggnet_device_object)
        return yggnet_device_object.mongo()

    @classmethod
    async def update_yggnet_device(cls, uid, update_yggnet_device_object: YggnetDevice):
        yggnet_devices = await YggnetDeviceCollection.get_yggnet_device(uid)
        if len(yggnet_devices) < 1:
            return False, "not exsist uid"
        result = await YggnetDeviceCollection.update_yggnet_device(uid, update_yggnet_device_object)
        return True, update_yggnet_device_object

    @classmethod
    async def delete_yggnet_device(cls, uid):
        yggnet_devices = await YggnetDeviceCollection.get_yggnet_device(uid)
        if len(yggnet_devices) < 1:
            return False, "not exsist uid"
        result = await YggnetDeviceCollection.delete_yggnet_device(uid)
        return True, "success"

    @classmethod
    async def get_yggnet_status(cls, uid = None):
        yggnet_status: List[YggnetStatus] = await YggnetStatusCollection.get_yggnet_status(uid)
        yggnet_device: List[YggnetDevice] = await YggnetDeviceCollection.get_yggnet_device(uid)
        yggnet_device_map = {}
        result = []
        for obj in yggnet_device:
            yggnet_device_map[obj.uid] = obj
        for each in yggnet_status:
            doc = each.mongo()
            doc.update(yggnet_device_map.get(each.uid).mongo())
            if doc.get('_id'):
                doc.pop('_id')
            result.append(doc)
        return result

    @classmethod
    async def upsert_yggnet_status(cls, yggnet_status_object: YggnetStatus):
        return await YggnetStatusCollection.upsert_yggnet_status(yggnet_status_object)

    @classmethod
    async def get_filtered_device(cls, field: str, value: Union[str, int], page: int, display_cnt: int):
        query = {}
        if field:
            query[field] = value

        total_doc_cnt = await YggnetDeviceCollection.get_count(query)
        res = {
            'docs': await YggnetDeviceCollection.get_yggnet_device_with_query(query, (page - 1) * display_cnt, display_cnt),
            'totalDocCnt': total_doc_cnt,
            'curPage': page,
        }
        return res