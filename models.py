from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from database import Base
from pydantic import BaseModel, Field, validator
from typing import List


#SQLAlchemy model for database representation
class Warrior(Base):
    __tablename__ = "warriors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dob = Column(String)
    fight_skills = Column(ARRAY(String))

# Pydantic model representing the basic structure of a warrior
class WarriorBase(BaseModel):
    name: str
    dob: str
    fight_skills: List[str] = Field(..., max_items=20, example=["Skill1", "Skill2"], min_items=1)

    class Config:
        orm_mode = True

    @validator('fight_skills')
    def check_length(cls, v):
        if len(v) > 20:
            raise ValueError('Max skills is 20')
        return v

# Pydantic model representing the data needed to create a warrior
class WarriorCreate(WarriorBase): #Changed from BaseModel to WarriorBase
    pass
    # name: str
    # dob: str
    # fight_skills: str
