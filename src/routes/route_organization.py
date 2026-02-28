from typing import Annotated
import uuid
from fastapi import APIRouter, Depends

from src.schemas.schema_organizations import CircleRequest
from src.services.service_organizations import ServiceOrganization


router = APIRouter(prefix="/organization", tags=["0rganizations"])
  
@router.get("/building/{id}")
def get_by_building_id(
    id: uuid.UUID
):
    service = ServiceOrganization()
    return service.get_by_building_id(id)

@router.get("/activity/{id}")
def get_by_activity_id(
    id: uuid.UUID
):
    service = ServiceOrganization()
    return service.get_by_activity_id(id)

@router.get("/range")
def get_by_range(
    data: Annotated[CircleRequest, Depends()]
):
    service = ServiceOrganization()
    return service.get_by_range(data)

@router.get("/activity_tree")
def get_by_activity_tree(
    name: str
):
    service = ServiceOrganization()
    return service.get_by_activity_tree(name)

@router.get("/name")
def get_by_name(
    name: str
):
    service = ServiceOrganization()
    return service.get_by_name(name)

@router.get("/{id}")
def get_by_id(
    id: uuid.UUID
):
    service = ServiceOrganization()
    return service.get_by_id(id)
