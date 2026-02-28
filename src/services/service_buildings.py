from sqlalchemy import select

from src.services.service_base import ServiceBase
from src.models.model_buildings import Buildings
from src.schemas.schema_buildings import BuildingSchema, FilterBuildings


class ServiceBuildings(ServiceBase):
    
    def get(self, filters: FilterBuildings):
        offset_value = filters.page * filters.limit

        stmt = (
            select(Buildings)
            .limit(filters.limit)
            .offset(offset_value)
        )

        result = self.session.execute(stmt)
        buildings = result.scalars().all()

        return [BuildingSchema.model_validate(building) for building in buildings]
    
