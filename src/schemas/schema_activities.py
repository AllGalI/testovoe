from typing import Optional
import uuid

from pydantic import BaseModel, ConfigDict, Field

class ActivitySchema(BaseModel):
    id: uuid.UUID
    name: str
    level: int = Field(ge=0, le=2)
    children: list["ActivitySchema"] = []

    model_config = ConfigDict(from_attributes=True)

ActivitySchema.model_rebuild()

