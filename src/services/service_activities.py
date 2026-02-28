from sqlalchemy import select

from src.models.model_activities import Activities
from src.schemas.schema_activities import ActivitySchema
from src.services.service_base import ServiceBase
from sqlalchemy.orm import selectinload


class ServiceActivities(ServiceBase):
    
    def get(self):
        stmt = (
            select(Activities)
            .where(Activities.level == 0)
            .options(
                selectinload(Activities.children)
                .selectinload(Activities.children)
            )
        )
        
        result = self.session.execute(stmt)
        activities_orm = result.scalars().unique().all()
        return [ActivitySchema.model_validate(activity) for activity in activities_orm]
    
