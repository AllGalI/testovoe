from typing import Annotated

from fastapi import APIRouter, Depends

from src.schemas.schema_buildings import BuildingSchema, FilterBuildings
from src.services.service_buildings import ServiceBuildings


router = APIRouter(prefix="/buildings", tags=["Buildings"])

@router.get("", response_model=list[BuildingSchema])
async def get(
    filters: Annotated[FilterBuildings, Depends()]
):
    service = ServiceBuildings()
    return service.get(filters)
