from sqlalchemy import Column, Integer, String
from database import Base

class Warrior(Base):
    __tablename__ = "warriors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dob = Column(String)
    fight_skills = Column(String)


class WarriorCreate(BaseModel):
    name: str
    dob: str
    fight_skills: str
    