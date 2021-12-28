from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel, Field
from src.models.mongodb_document import MongodbBaseModel


class PostNinesApiAccessKey(MongodbBaseModel):
    referer: str = Field(default="", title="referer", description="")
    expire_time: datetime = Field(default=None, title="expire time", description="")

