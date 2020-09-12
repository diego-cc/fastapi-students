"""
Project: fastapi-students
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 12/09/2020 4:55 pm
File: actions.py
"""
from sqlalchemy.orm import Session
from . import models, schemas


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_student_by_email(db: Session, student_email: str):
    return db.query(models.Student).filter(models.Student.email == student_email).first()


def create_student(db: Session, student:schemas.StudentCreate):
    db_student = models.Student(name=student.name, email=student.email, password=student.password)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db: Session, student_id: int, student: schemas.StudentUpdate):
    db_student = get_student_by_id(db=db, student_id=student_id)
    db_student.name = student.name
    db_student.email = student.email
    db_student.password = student.password
    db_student.is_active = student.is_active
    db.commit()
    db.refresh(db_student)
    return db_student


def delete_student(db: Session, student_id: int):
    db_student = get_student_by_id(db=db, student_id=student_id)
    db.delete(db_student)
    db.commit()
    return db_student
