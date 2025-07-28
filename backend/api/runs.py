from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.database import SessionLocal
from backend.models import Run as RunModel
from backend.schemas import Run, RunCreate

router = APIRouter(prefix="/api/runs", tags=["runs"])

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Run])
def read_runs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    runs = db.query(RunModel).offset(skip).limit(limit).all()
    return runs

@router.post("/", response_model=Run)
def create_run(run: RunCreate, db: Session = Depends(get_db)):
    db_run = RunModel(**run.model_dump())
    db.add(db_run)
    db.commit()
    db.refresh(db_run)
    return db_run

@router.get("/{run_id}", response_model=Run)
def read_run(run_id: int, db: Session = Depends(get_db)):
    run = db.query(RunModel).filter(RunModel.id == run_id).first()
    if run is None:
        raise HTTPException(status_code=404, detail="Run not found")
    return run