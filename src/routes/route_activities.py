from fastapi import APIRouter

from src.schemas.schema_activities import ActivitySchema
from src.services.service_activities import ServiceActivities

router = APIRouter(prefix="/activities", tags=["Activities"])
@router.get("", response_model=list[ActivitySchema])
async def get():
    service = ServiceActivities()
    return service.get()
