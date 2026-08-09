from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware # 1. Import CORS tools
from sqlalchemy.orm import Session
from typing import List
from database import get_db, engine
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 2. Configure CORS allowances
# This tells your FastAPI backend to trust your Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],  # ◄— Explicitly lists both common local web addresses
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"status": "success", "message": "School Management API is online!"}

@app.get("/api/students", response_model=List[schemas.StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

@app.post("/api/students", response_model=schemas.StudentResponse)
def create_new_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    existing_student = db.query(models.Student).filter(models.Student.reg_no == student.reg_no).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Registration number already registered.")
        
    db_student = models.Student(
        first_name=student.first_name,
        middle_name=student.middle_name,
        surname=student.surname,
        email=student.email,
        reg_no=student.reg_no,
        date_of_birth=student.date_of_birth
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student