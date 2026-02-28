



import uuid
from decimal import Decimal, ROUND_HALF_UP
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import aliased, selectinload

from src.models.model_activities import Activities, ActivityTree
from src.models.model_buildings import Buildings
from src.models.model_organizations import Organizations, Phones
from src.schemas.schema_organizations import CircleRequest, OrganizationDetailSchema, OrganizationSchema
from src.services.service_base import ServiceBase


class ServiceOrganization(ServiceBase):
    def get_by_building_id(self, id: uuid.UUID) -> list[OrganizationSchema]:
        stmt = (
            select(Organizations)
            .select_from(Buildings)
            .where(Buildings.id == id)
            .join(Organizations, Buildings.id == Organizations.building_id)
        )

        result = self.session.execute(stmt)
        organizations = result.scalars().all()

        return [OrganizationSchema.model_validate(organization) for organization in organizations]

    def get_by_activity_id(self, id: uuid.UUID) -> list[OrganizationSchema]:
        stmt = (
            select(Organizations)
            .select_from(Activities)
            .where(Activities.id == id)
            .join(Organizations, Activities.id == Organizations.activity_id)
        )

        result = self.session.execute(stmt)
        organizations = result.scalars().all()

        return [OrganizationSchema.model_validate(organization) for organization in organizations]

    def get_by_range(self, data: CircleRequest):

        lat = Decimal(str(data.lat))
        lon = Decimal(str(data.lon))
        radius = Decimal(str(data.radius))
        
        # Определяем формат округления (6 знаков)
        precision = Decimal('0.000001')

        # Вычисляем границы
        raw_min_lat = lat - radius
        raw_max_lat = lat + radius
        raw_min_lon = lon - radius
        raw_max_lon = lon + radius

        # Округляем "в ближайшую сторону" (0.0000005 станет 0.000001)
        min_lat = raw_min_lat.quantize(precision)
        max_lat = raw_max_lat.quantize(precision)
        min_lon = raw_min_lon.quantize(precision)
        max_lon = raw_max_lon.quantize(precision)

        stmt = (
            select(Organizations)
            .select_from(Buildings)
            .where(
                Buildings.lat >= min_lat,
                Buildings.lat <= max_lat,
                Buildings.lon >= min_lon,
                Buildings.lon <= max_lon,
            )
            .join(Organizations, Buildings.id == Organizations.building_id)
        )

        result = self.session.execute(stmt)
        organizations = result.scalars().all()

        return [OrganizationSchema.model_validate(organization) for organization in organizations]
        
        

    def get_by_id(self, id: uuid.UUID) -> OrganizationDetailSchema:
        stmt = (
            select(Organizations)
            .where(Organizations.id == id)
            .options(
                selectinload(Organizations.phones).load_only(Phones.number),
                selectinload(Organizations.activity),
                selectinload(Organizations.building)
            )
        )
        result = self.session.execute(stmt)
        orm_data = result.scalar_one_or_none()

        if orm_data is None:
            raise HTTPException(404, "organization not exists")

        return OrganizationDetailSchema(
            id=orm_data.id,
            name=orm_data.name,
            building_id=orm_data.building_id,
            activity_id=orm_data.activity_id,
            phones=[phone.number for phone in orm_data.phones],
            building=orm_data.building,
            activity=orm_data.activity
        )


    def get_by_activity_tree(self, name):
        anchor = (
            select(Activities.id.label("activity_id"))
            .where(Activities.name == name)
            .cte(name="all_descendants", recursive=True)
        )

        recursive_part = (
            select(ActivityTree.child_id.label("activity_id"))
            .join(anchor, ActivityTree.parent_id == anchor.c.activity_id)
        )

        all_descendants_cte = anchor.union_all(recursive_part)

        stmt = (
            select(Organizations)
            .distinct()
            .where(Organizations.activity_id.in_(select(all_descendants_cte.c.activity_id)))
        )

        result = self.session.execute(stmt)
        organizations = result.scalars().all()

        return [OrganizationSchema.model_validate(organization) for organization in organizations]

    def get_by_name(self, name: str)-> OrganizationSchema:
        stmt = (
            select(Organizations)
            .where(Organizations.name == name)
            .options(
                selectinload(Organizations.phones).load_only(Phones.number),
                selectinload(Organizations.activity),
                selectinload(Organizations.building)
            )
        )

        result = self.session.execute(stmt)
        orm_data = result.scalar_one_or_none()

        if orm_data is None:
            raise HTTPException(404, "organization not exists")        

        return OrganizationDetailSchema(
            id=orm_data.id,
            name=orm_data.name,
            building_id=orm_data.building_id,
            activity_id=orm_data.activity_id,
            phones=[phone.number for phone in orm_data.phones],
            building=orm_data.building,
            activity=orm_data.activity
        )