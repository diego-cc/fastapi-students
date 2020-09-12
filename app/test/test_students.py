"""
Project: fastapi-students
Author: Diego C. <20026893@tafe.wa.edu.au>
Created at: 12/09/2020 4:56 pm
File: test_students.py
"""
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..db import Base
from ..main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///.test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_student():
    response = client.post(
        "/students",
        json={"name": "Richard", "email": "rich@mail.com", "password": "password123"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "rich@mail.com"
    assert "id" in data
    student_id = data["id"]

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "rich@mail.com"
    assert data["id"] == student_id


def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data) == 1
    assert data[0]["email"] == "rich@mail.com"


"""
For some reason, there's no "json" parameter that can be passed to client.put() (from fastapi.testclient)
def test_update_student():
    response = client.put(
        "/students/1",
        data={"name": "John", "email": "john@doe.com", "password": "whatever_m8", "is_active": True}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "john@doe.com"
    assert "id" in data
    assert data["id"] == 1
"""
