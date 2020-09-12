"""
Project: fastapi-students
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 12/09/2020 4:55 pm
File: models.py
"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(128))
    is_active = Column(Boolean, default=True)

