
from sqlalchemy import Column, Integer, DateTime, String
from ..database import Base


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    create_at = Column(DateTime)
