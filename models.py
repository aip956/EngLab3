from sqlalchemy import Column, Integer, String
from database import Base
from pydantic import BaseModel

#SQLAlchemy model for database representation
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
        orm_mode = True

# Pydantic model representing the complete structure of a warrior
# class DetailedWarrior(WarriorBase):
#     class Config:
#         orm_mode = True

# Pydantic model representing the data needed to create a warrior
class WarriorCreate(WarriorBase): #Changed from BaseModel to WarriorBase
    name: str
    dob: str
    fight_skills: str
