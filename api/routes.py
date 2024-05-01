from typing import List, Optional, Dict

from fastapi import HTTPException, Query, Depends, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session

from models import Warrior, WarriorBase, WarriorCreate
from database import get_db

router = APIRouter()


# Endpoint to get warrior by ID
@router.get("/warrior/{id}", response_model=WarriorBase)
def get_warrior_by_id(id: int, db: Session = Depends(get_db)) -> WarriorBase:
    warrior = db.query(Warrior).filter(Warrior.id == id).first()
    if warrior is None:
        raise HTTPException(status_code=404, detail="Warrior not found")
    return warrior


# Endpoint to search warriors by attributes
@router.get("/warrior", response_model=List[WarriorBase])
def search_warriors(db: Session = Depends(get_db),
                    t: Optional[str] = Query(None, description="Search term")) -> List[WarriorBase]:
    if t is None:
        warriors = db.query(Warrior).all()
        if not warriors:
            raise HTTPException(status_code=404, detail="No warriors found")
        return warriors

    filtered_warriors = db.query(Warrior).filter(
        func.lower(Warrior.name).contains(func.lower(t))
    ).all()

    if filtered_warriors:
        return filtered_warriors
    else:
        raise HTTPException(status_code=404, detail="No matching warriors found")


# Endpoint to count registered warriors
@router.get("/counting-warriors")
def count_warriors(db: Session = Depends(get_db)) -> Dict[str, int]:
    count = db.query(Warrior).count()
    return {"Count: ": count}


# Endpoint to create a warrior
@router.post("/warrior", response_model=WarriorBase)
def create_warrior(warrior: WarriorCreate, db: Session = Depends(get_db)) -> WarriorBase:
    db_warrior = Warrior(**warrior.dict())
    db.add(db_warrior)
    db.commit()
    db.refresh(db_warrior)
    return db_warrior
