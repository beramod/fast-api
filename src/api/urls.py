from fastapi import APIRouter

from .machine.machine_v1 import machine_v1_router
from .session.session_v1 import session_v1_router
from .yggnet.yggnet_v1 import yggnet_v1_router

router = APIRouter()

router.include_router(
    machine_v1_router,
    prefix='/v1/machine',
    tags=['machine']
)

router.include_router(
    session_v1_router,
    prefix='/v1/session',
    tags=['session']
)


router.include_router(
    yggnet_v1_router,
    prefix='/v1/yggnet',
    tags=['yggnet']
)
