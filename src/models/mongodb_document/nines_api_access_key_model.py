from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel, Field
from src.models.mongodb_document import MongodbBaseModel

class NinesApiAccessKey(MongodbBaseModel):
    referer: str = Field(default="", title="referer", description="")
    api_key: str = Field(default="", title="api key", description="", alias="apiKey")
    created_user_id: str = Field(default="", title="created user id", description="", alias="createdUserId")
    generate_key_time: str = Field(default="", title="generate key time", description="", alias="generateKeyTime")
    expire_time: datetime = Field(default=None, title="expire time", description="", alias="expireTime")

