from src.models.mongodb_document import MongodbBaseModel
from datetime import datetime

class ConnectionInfo:
    def __init__(self):
        self.ip: str = None
        self.ssh: int = None
        self.user: str = None
        self.password: str = None

class Machine(MongodbBaseModel):
    def __init__(self):
        self.host_name: str = None
        self.mcno: int = None
        self.role: str = None
        self.status: str = None
        self.brand: str = None
        self.model: str = None
        self.cpu: str = None
        self.core: int = None
        self.memory: int = None
        self.storage_brand: str = None
        self.storage_model: str = None
        self.storage_type: str = None
        self.storage_size: str = None
        self.os: str = None
        self.model_year: str = None
        self.serverName: str = None
        self.connectionInfo = ConnectionInfo()

    def makeQueryDict(self):
        result = {}
        for member in [attr for attr in dir(self) if
                       not callable(getattr(self, attr)) and not attr.startswith("__") and getattr(self,
                                                                                                   attr) is not None]:
            if member in ['hostName', 'role']:
                result[member] = {'$regex': getattr(self, member)}
            else:
                result[member] = getattr(self, member)

        return result


class MachineSearch:
    def __init__(self):
        self.keyword: str = None
        self.keyword_mcnos: list[int] = None
        self.check_role: str = None
        self.check_status: str = None
        self.from_date: str = None
        self.to_date: str = None
        self.search_date_field: str = None

    def makeQueryDict(self):
        query = {}
        for member in [attr for attr in dir(self) if
                       not callable(getattr(self, attr)) and not attr.startswith("__") and getattr(self,
                                                                                                   attr) is not None]:
            if member not in ['keyword', 'keyword_mcnos', 'check_role', 'check_status', 'from_date', 'to_date',
                              'search_date_field']:
                query[member] = getattr(self, member)

        if self.from_date and self.to_date:
            search_date_field = self.search_date_field
            from_datetime_at = datetime.strptime('20' + self.from_date + '000000.000000', '%Y%m%d%H%M%S.%f')
            to_datetime_at = datetime.strptime('20' + self.to_date + '235959.000000', '%Y%m%d%H%M%S.%f')
            query[search_date_field] = {'$gte': from_datetime_at, '$lte': to_datetime_at}

        if self.keyword is not None:
            keyword = self.keyword
            or_condition = []
            or_condition.append({'hostName': {'$regex': keyword}})
            or_condition.append({'serverName': {'$regex': keyword}})
            or_condition.append(
                {'$expr': {'$regexMatch': {'input': {'$toString': '$mcno'}, 'regex': '.*' + keyword + '.*'}}})
            or_condition.append({'status': {'$regex': keyword}})
            or_condition.append({'brand': {'$regex': keyword}})
            or_condition.append({'model': {'$regex': keyword}})
            or_condition.append({'ip': {'$regex': keyword}})
            or_condition.append({'ip2': {'$regex': keyword}})
            or_condition.append({'storageBrand': {'$regex': keyword}})
            or_condition.append({'storageModel': {'$regex': keyword}})
            or_condition.append({'modelYear': {'$regex': keyword}})
            # or_condition.append({'mcno': {'$in': self.keyword_mcnos}})
            query['$or'] = or_condition

        if self.check_role:
            query['role'] = {'$in': self.check_role}

        if self.check_status:
            query['status'] = {'$in': self.check_status}

        return query
