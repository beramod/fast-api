import datetime
from typing import List
from pydantic import BaseModel, Field
from src.models.mongodb_document import MongodbBaseModel

class YggnetPacketHistory(BaseModel):
    packet_type: int = Field(default=0, alias="packetType")
    packet_in_cnt: int = Field(default=0, alias="packetInCnt")
    packet_out_cnt: int = Field(default=0, alias="packetOutCnt")
    packet_in_bytes: int = Field(default=0, alias="packetInBytes")
    packet_out_bytes: int = Field(default=0, alias="packetOutBytes")

class YggnetInfo(BaseModel):
    uid: str = Field(default="", title="uid", description="")
    packet_history: List[YggnetPacketHistory] = Field(default=None, title="packet history", description="", alias="packetHistory")
    last_check_time: datetime.datetime = Field(default=None, title="last check time", description="", alias="lastCheckTime")
    response_time: float = Field(default=0.0, title="response time", description="", alias="responseTime")

class YggnetStatus(MongodbBaseModel):
    uid: str = Field(default="", title="uid", description="")
    lora_table: List[YggnetInfo] = Field(default=None, title="Lora Info", desciption="", alias="loraTable")