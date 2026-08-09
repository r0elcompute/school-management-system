from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional, List

# --- STUDENT SCHEMAS ---

# 1. Base properties shared when reading or writing student data
class StudentBase(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    surname: str
    email: str  # Validates it's a structural string
    reg_no: str
    date_of_birth: date # Ensures incoming payload is a proper YYYY-MM-DD date

# 2. What data is REQUIRED when a user fills out a registration form
class StudentCreate(StudentBase):
    pass # It requires exactly what is in StudentBase

# 3. What data FastAPI sends BACK to the Next.js frontend
class StudentResponse(StudentBase):
    id: int
    created_at: datetime

    class Config:
        # Crucial: Tells Pydantic to read database records smoothly 
        # even though they are SQLAlchemy models, not Python dictionaries.
        from_attributes = True
