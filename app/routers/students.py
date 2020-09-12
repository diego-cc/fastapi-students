"""
Project: fastapi-students
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 12/09/2020 5:00 pm
File: students.py
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/students", tags=["students"])
async def read_students():
    pass


@router.get("/students/{student_id}", tags=["students"])
async def read_student(student_id: int):
    pass


