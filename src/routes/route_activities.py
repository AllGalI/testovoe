from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.configs.db import get_async_session
from src.schemas.schema_activities import ActivitySchema
from src.services.service_activities import ServiceActivities

router = APIRouter(prefix="/activities", tags=["Activities"])
@router.get("", response_model=list[ActivitySchema])
async def get(session: AsyncSession = Depends(get_async_session)):
    service = ServiceActivities(session)
    return await service.get()
