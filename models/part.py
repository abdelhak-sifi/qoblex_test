from sqlalchemy import Column, Integer, String
from models.base import Base

class Part(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False) # for define type of part leaf or bundle
    stock = Column(Integer, nullable=True)  # stock of leaf 
