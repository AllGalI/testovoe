import uuid

from sqlalchemy import UUID, CheckConstraint, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .model_base import Base


class ActivityTree(Base):
    parent_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("activities.id", ondelete="CASCADE"), nullable=True)
    child_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("activities.id", ondelete="CASCADE"), nullable=True)

class Activities(Base):
    name: Mapped[str] = mapped_column(String, nullable=False)
    level: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    parent: Mapped["Activities"] = relationship(
        'Activities',
        secondary="activitytree",
        primaryjoin=lambda: Activities.id == ActivityTree.child_id,
        secondaryjoin=lambda: Activities.id == ActivityTree.parent_id,
        back_populates='children'
    )
    
    children: Mapped[list["Activities"]] = relationship(
        "Activities",
        secondary="activitytree",
        primaryjoin=lambda: Activities.id == ActivityTree.parent_id,
        secondaryjoin=lambda: Activities.id == ActivityTree.child_id,
        back_populates="parent"
    )
    
    organizations: Mapped[list["Organizations"]] = relationship(
        "Organizations",
        back_populates="activity"
    )

    __table_args__ = (
        UniqueConstraint(
            "name",
            name="uq_activities_name",
            postgresql_nulls_not_distinct=True
        ),
        CheckConstraint("level >= 0 AND level <= 2", name="check_level_range"),
    )