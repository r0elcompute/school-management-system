import os
import urllib.parse
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DB_PASSWORD = os.getenv("DATABASE_PASSWORD")

# This is the line that converts the '@' symbol safely
ENCODED_PASSWORD = urllib.parse.quote_plus(DB_PASSWORD)

DATABASE_URL = f"postgresql://postgres:{ENCODED_PASSWORD}@localhost:5432/school_database"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
