from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "School Management API is online!"}

@app.get("/api/db-test")
def test_db_connection(db: Session = Depends(get_db)):
    # This executes a simple check against your PostgreSQL database
    try:
        db.execute("SELECT 1")
        return {"status": "success", "database": "Connected successfully!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
