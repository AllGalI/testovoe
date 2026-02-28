import uuid

from pydantic import BaseModel, ConfigDict, Field

class BuildingSchema(BaseModel):
    id: uuid.UUID
    address: str
    lon: float
    lat: float

    model_config = ConfigDict(from_attributes=True)


class FilterBuildings(BaseModel):
    page: int = Field(0)
    limit: int = Field(20)