from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel, Field
from src.models.mongodb_document.location import Location
from src.models.mongodb_document import MongodbBaseModel

class YggnetDevice(MongodbBaseModel):
    serial_number: str = Field(default="", title="S/N", description="", alias="serialNumber")
    uid: str = Field(default="", title="uid", description="")
    device_type: str = Field(default="", title="lora device type", description="1: LoryGate, 2: sLory or uLory", alias="deviceType")
    mcno: int = Field(default=None, title="mcno", description="device type이 2인 경우에만 사용")
    device_id: str = Field(default="", title="device id", description="dt 1: 00000 ~ 99999, dt 2: 000 ~ 999", alias="deviceId")
    memo: str = Field(default="", title="memo")
    location: Location = Field(default=None, title="location", description="설치된 위치")

