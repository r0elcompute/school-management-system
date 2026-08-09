from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db, engine
import models
import schemas # Import your new validation layout

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "School Management API is online!"}

# NEW ROUTE: Fetch all students from the database safely validated by your Schema
@app.get("/api/students", response_model=List[schemas.StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    # 1. Query all records inside the postgres 'students' table
    students = db.query(models.Student).all()
    
    # 2. FastAPI automatically passes this through StudentResponse schemas
    return students
