import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load the secret environment variables from the .env file
load_dotenv()

# Safely fetch the password from your machine's environment
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")

# Dynamically insert the password into your connection string
DATABASE_URL = f"postgresql://postgres:{DB_PASSWORD}@localhost:5432/school_management"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
