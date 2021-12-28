from motor.motor_asyncio import AsyncIOMotorClient
from src import settings

class MongoDB:
    def __init__(self):
        self._host_hot = None
        self._host_temp = None
        self._host_heesung = None
        self._client_hot = None
        self._client_tmep = None
        self._client_heesung = None
        self._env = None

    def set_hosts(self, env):
        self._env = env
        self._host_temp = '{cache db}'
        self._host_heesung = \
            '{hs db}'
        if self._env == 'PROD' or self._env == 'STAGE':
            self._host_hot = '{hot}'
        elif self._env == 'DEV':
            self._host_hot = '{dev db}'
        else:
            self._host_hot = '{aws ssh tunneling}'
            self._host_temp = '{aws ssh tunneling}'

    def set_client(self):
        max_pool_size = 10
        min_pool_size = 10
        self._client_hot = AsyncIOMotorClient(self._host_hot, maxPoolSize=max_pool_size, minPoolSize=min_pool_size)
        self._client_temp = AsyncIOMotorClient(self._host_temp, maxPoolSize=max_pool_size, minPoolSize=min_pool_size)
        self._client_heesung = AsyncIOMotorClient(self._host_heesung, maxPoolSize=max_pool_size, minPoolSize=min_pool_size)

    def close(self):
        if self._client_hot:
            self._client_hot.close()
        if self._client_temp:
            self._client_temp.close()
        if self._client_heesung:
            self._client_heesung.close()

    def get_client(self, host):
        if host == 'hot':
            return self._client_hot
        elif host == 'temp':
            return self._client_temp
        elif host == 'heesung':
            return self._client_heesung
        return None

db = MongoDB()

def get_client(host):
    return db.get_client(host)

def close_db():
    db.close()

def set_db():
    db.set_hosts(settings.ENV)
    db.set_client()