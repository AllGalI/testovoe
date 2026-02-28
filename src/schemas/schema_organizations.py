import uuid

from pydantic import BaseModel, ConfigDict

from src.schemas.schema_activities import ActivitySchema
from src.schemas.schema_buildings import BuildingSchema

class OrganizationSchema(BaseModel):
    id: uuid.UUID
    name: str
    building_id: uuid.UUID
    activity_id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)


class OrganizationDetailSchema(BaseModel):
    id: uuid.UUID
    name: str
    building_id: uuid.UUID
    activity_id: uuid.UUID
    phones: list[str]
    building: BuildingSchema
    activity: ActivitySchema

    model_config = ConfigDict(from_attributes=True)
    

class CircleRequest(BaseModel):
    lat: float
    lon: float
    radius: float
