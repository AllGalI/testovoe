from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .model_base import Base


class Buildings(Base):
    address: Mapped[str] = mapped_column(String, nullable=False)
    lon: Mapped[float] = mapped_column(Float, nullable=False)
    lat: Mapped[float] = mapped_column(Float, nullable=False)
    
    organizations: Mapped[list["Organizations"]] = relationship(
        "Organizations",
        back_populates="building"
    )
