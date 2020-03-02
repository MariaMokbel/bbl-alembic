from sqlalchemy import Column, TIMESTAMP, String, Integer, ForeignKey, DateTime, CheckConstraint, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum

Base = declarative_base()


class Consultant(Base):
    __tablename__ = 'consultant'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)


class Mission(Base):
    __tablename__ = 'mission'
    id = Column(Integer, primary_key=True)
    location = Column(String, nullable=False)
    client = Column(String, nullable=False)