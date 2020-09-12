"""
Project: fastapi-students
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 12/09/2020 4:55 pm
File: schemas.py
"""
from pydantic import BaseModel


class StudentBase(BaseModel):
    name: str
    email: str


class StudentCreate(StudentBase):
    password: str


class Student(StudentBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
