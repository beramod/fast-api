from datetime import datetime
from pydantic import BaseModel, Field, BaseConfig
from bson.objectid import ObjectId


class MongodbBaseModel(BaseModel):
    # id: ObjectId = Field(description = "document id")
    createdAt: datetime = Field(default=None, description = "document created date")
    updatedAt: datetime = Field(default=None, description = "document last updated date")

    class Config(BaseConfig):
        # allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
            ObjectId: lambda oid: str(oid),
        }

    @classmethod
    def from_mongo(cls, data: dict):
        if not data:
            return data
        id = data.pop('_id', None)
        return cls(**dict(data, id=id))

    def mongo(self, **kwargs):
        exclude_unset = kwargs.pop('exclude_unset', True)
        by_alias = kwargs.pop('by_alias', True)

        parsed = self.dict(
            exclude_unset=exclude_unset,
            by_alias=by_alias,
            **kwargs,
        )

        # Mongo uses `_id` as default key. We should stick to that as well.
        if '_id' not in parsed and 'id' in parsed:
            parsed['_id'] = parsed.pop('id')

        return parsed