from datetime import datetime
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from src.api.session import SessionBaseController
from src.api.session.services import SessionHandler
from src.models.request.post_api_key import PostNinesApiAccessKey
session_v1_router = InferringRouter()
from starlette.requests import Request

@cbv(session_v1_router)
class SessionController(SessionBaseController):
    @session_v1_router.get("/api-key", tags=["nines-access-key", "@QUOTA:50/300"])
    async def get_nines_access_key(self, api_key: str = None):
        response = await SessionHandler.get_nines_access_key(api_key)
        return {"result": response, 'message': '', 'code': 200}

    @session_v1_router.post("/api-key", tags=["nines-access-key"])
    async def create_nines_access_key(self, api_key_object: PostNinesApiAccessKey, request: Request):
        response = await SessionHandler.create_nines_access_key(api_key_object.referer, api_key_object.expire_time,
                                                                request.state.session.get('id'))
        return {"result": response, 'message': '', 'code': 200}

    @session_v1_router.delete("/api-key", tags=["nines-access-key"])
    async def delete_nines_access_key(self, api_key):
        response = await SessionHandler.delete_nines_api_key(api_key)
        return {"result": response, 'message': '', 'code': 200}
