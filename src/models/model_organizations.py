import uuid

from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .model_base import Base


class Organizations(Base):
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    building_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("buildings.id", ondelete="SET NULL"), nullable=False)
    activity_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("activities.id", ondelete="SET NULL"), nullable=False)

    phones: Mapped[list["Phones"]] = relationship(
        "Phones",
        back_populates="organization",  
        cascade="all, delete-orphan"  
    )

    building: Mapped["Buildings"] = relationship(
        "Buildings",
        back_populates="organizations"
    )
    
    activity: Mapped["Activities"] = relationship(
        "Activities",
        back_populates="organizations"
    )
    

class Phones(Base):
    number: Mapped[str] = mapped_column(String, nullable=False)
    organization_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False)

    organization: Mapped["Organizations"] = relationship(
        "Organizations",
        back_populates="phones"
    )
