from pydantic import BaseModel, Field, validator,ValidationError 
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from database import Base
from typing import List
import datetime


# SQLAlchemy model for database representation
class Warrior(Base):
    __tablename__ = "warriors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dob = Column(String)
    fight_skills = Column(ARRAY(String))


# Pydantic model representing the basic structure of a warrior
class WarriorBase(BaseModel):
    name: str = Field(..., max_length=100)
    dob: datetime.date = Field(...)
    fight_skills: List[str]=Field(..., max_items=20)

    # @validator('dob', pre=True)
    # def parse_dob(cls, value: str):
    #     try:
    #         # Ensure data is in the right format
    #         return datetime.datetime.strptime(value, "%Y-%d-%m").date()
    #     except ValueError as e:
    #         raise ValueError("dob must be in format YYYY-DD-MM") from e
        
    # @validator('fight_skills', each_item=True)
    # def check_skill_length(cls, v):
    #     if len(v) > 250:
    #         raise ValueError('Each fight skill must not exceed 250 chars')
    #     return v
    class Config:
        from_attributes = True

# Pydantic model representing the data needed to create a warrior
class WarriorCreate(WarriorBase):
    pass

