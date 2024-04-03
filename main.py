from fastapi import FastAPI, HTTPException, Query, Depends
from typing import List, Optional
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from sqlalchemy import func
from models import Base, Warrior, WarriorBase, WarriorCreate

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to get warrior by ID
@app.get("/warrior/{id}", response_model=WarriorBase)
def get_warrior_by_id(id: int, db: Session = Depends(get_db)):
    warrior = db.query(Warrior).filter(Warrior.id == id).first()
    if warrior is None:
        raise HTTPException(status_code=404, detail="Warrior not found")
    return warrior

# Endpoint to search warriors by attributes
@app.get("/warrior", response_model=List[WarriorBase])
def search_warriors(
    db: Session = Depends(get_db),
    t: Optional[str] = Query(None, description="Search term")
):
    if t is None:
        return db.query(Warrior).all()
    return db.query(Warrior).filter(
        func.lower(Warrior.name).contains(func.lower(t))
    ).all()

# Endpoint to count registered warriors
@app.get("/counting-warriors")
def count_warriors(db: Session = Depends(get_db)):
    return db.query(Warrior).count()

# Endpiont to create a warrior
@app.post("/warrior", response_model=WarriorBase)
def create_warrior(warrior: WarriorCreate, db: Session = Depends(get_db)):
    db_warrior = Warrior(**warrior.dict())
    db.add(db_warrior)
    db.commit()
    db.refresh(db_warrior)
    return db_warrior
