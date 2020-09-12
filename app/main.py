from typing import List

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

from . import actions, schemas, models
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

"""
Dependency with middleware, as an alternative to using generators (see below)
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
    
    
def get_db(request: Request):
    return request.state.db
"""

"""
Dependency with generators, requires async-exit-stack and async-generator packages to work if using Python < 3.7
"""


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/students", response_model=List[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = actions.get_students(db=db, skip=skip, limit=limit)
    return students


@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student_by_id(student_id: int, db: Session = Depends(get_db)):
    db_student = actions.get_student_by_id(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.post("/students", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return actions.create_student(db=db, student=student)


@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student: schemas.StudentUpdate, student_id: int, db: Session = Depends(get_db)):
    return actions.update_student(db=db, student_id=student_id, student=student)


@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return actions.delete_student(db=db, student_id=student_id)
