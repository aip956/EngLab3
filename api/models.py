from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from database import Base


# SQLAlchemy model for database representation
class Warrior(Base):
    __tablename__ = "warriors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dob = Column(String)
    fight_skills = Column(String)


# Pydantic model representing the basic structure of a warrior
class WarriorBase(BaseModel):
    name: str
    dob: str
    fight_skills: str

    class Config:
        from_attributes = True


# Pydantic model representing the data needed to create a warrior
class WarriorCreate(WarriorBase):
    pass
