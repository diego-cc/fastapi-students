"""
Project: fastapi-students
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 12/09/2020 4:55 pm
File: db.py
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://students_admin:Password1@localhost/fastapi_students'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

