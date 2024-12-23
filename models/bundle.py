from sqlalchemy import Column, ForeignKey, Integer
from models.base import Base

class Bundle(Base):
    __tablename__ = "bundles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey("parts.id"), nullable=False)
    child_id = Column(Integer, ForeignKey("parts.id"), nullable=False)
    quantity_needed = Column(Integer, nullable=False)
