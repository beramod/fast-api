from fastapi import APIRouter

from .exam.exam_v1 import exam_v1_router
from .module.router import module_router
from .weather.weather_v1 import weather_v1_router
from .machine_index.machine_index_v1 import machine_index_v1_router
from .pms.router import pms_router
from .nines.monitoring.monitoring_v1 import monitoring_v1_router
from .nines.router import nines_router
from .statistics.statistice_v1 import statistics_v1_router
from .machine_index.router import machine_index_router
from .search.search_v1 import search_v1_router
from .machine.machine_v1 import machine_v1_router
from .shell.shell_v1 import shell_v1_router
from .meta.power_station.power_station_v1 import power_station_v1_router
from .devops.connect_info_v1 import devops_v1_router
from .labs.labs_v1 import labs_v1_router
from .poc.poc_v1 import poc_v1_router
from .session.session_v1 import session_v1_router
from .event.event_v1 import event_v1_router
from .meta.router import meta_router
from .meta.collect_module_info.collect_module_info_v1 import collect_module_info_v1_router
from .proxy.proxy_v1 import proxy_v1_router
from .yggnet.yggnet_v1 import yggnet_v1_router
from .flow.flow_v1 import flow_v1_router
from .user.user_v1 import user_v1_router


router = APIRouter()
router.include_router(
    exam_v1_router,
    prefix="/v1/exam",
    tags=["exam"]
)
router.include_router(
    module_router,
    prefix="/v1/module",
    tags=["module"]
)

router.include_router(
    weather_v1_router,
    prefix='/v1/weather',
    tags=['weather']
)

router.include_router(
    machine_index_router,
    prefix="/v1/machine-index-category",
    tags=["machine-index", "category"]
)

router.include_router(
    machine_index_v1_router,
    prefix="/v1/machine-index",
    tags=["machine-index"]
)
# router.include_router(bms_v1_router)

router.include_router(
    pms_router,
    prefix='/v1/pms',
    tags=['pms']
)

router.include_router(
    nines_router,
    prefix='/v1/nines',
    tags=['nines']
)

router.include_router(
    monitoring_v1_router,
    prefix='/v1/monitoring',
    tags=['monitoring']
)

router.include_router(
    statistics_v1_router,
    prefix='/v1/statistics',
    tags=['statistics']
)

router.include_router(
    search_v1_router,
    prefix='/v1/search',
    tags=['search']
)

router.include_router(
    machine_v1_router,
    prefix='/v1/machine',
    tags=['machine']
)

router.include_router(
    power_station_v1_router,
    prefix='/v1/power-station',
    tags=['power_station']
)

router.include_router(
    shell_v1_router,
    prefix='/v1/shell',
    tags=['shell']
)

router.include_router(
    devops_v1_router,
    prefix='/v1/devops',
    tags=['devops']
)

router.include_router(
    labs_v1_router,
    prefix='/v1/labs',
    tags=['labs']
)

router.include_router(
    poc_v1_router,
    prefix='/v1/poc',
    tags=['poc']
)

router.include_router(
    session_v1_router,
    prefix='/v1/session',
    tags=['session']
)

router.include_router(
    event_v1_router,
    prefix='/v1/event',
    tags=['event']
)
router.include_router(
    collect_module_info_v1_router,
    prefix='/v1/collect-module-info',
    tags=['collect-module-info']
)

router.include_router(
    meta_router,
    prefix='/v1/meta',
    tags=['meta']
)

router.include_router(
    proxy_v1_router,
    prefix='/v1/proxy',
    tags=['proxy']
)

router.include_router(
    yggnet_v1_router,
    prefix='/v1/yggnet',
    tags=['yggnet']
)

router.include_router(
    flow_v1_router,
    prefix='/v1/flow',
    tags=['flow']
)

router.include_router(
    user_v1_router,
   prefix='/v1/user',
   tags=['user']
)