from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

# 1. DEPARTMENTS TABLE
class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    # Relationships
    teachers = relationship("Teacher", back_populates="department")


# 2. TEACHERS TABLE
class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=True)
    surname = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    staff_no = Column(String(50), unique=True, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    department = relationship("Department", back_populates="teachers")
    classes = relationship("Class", back_populates="teacher")


# 3. COURSES TABLE
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String(50), unique=True, nullable=False)
    course_name = Column(String(255), nullable=False)
    credits = Column(Integer, nullable=False)

    # Relationships
    classes = relationship("Class", back_populates="course")


# 4. CLASSES TABLE
class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    teachers_id = Column(Integer, ForeignKey("teachers.id"), nullable=False) # Maps to image constraint name
    semester = Column(String(50), nullable=False)
    room = Column(String(50), nullable=True)

    # Relationships
    course = relationship("Course", back_populates="classes")
    teacher = relationship("Teacher", back_populates="classes")
    enrollments = relationship("Enrollment", back_populates="class_")


# 5. STUDENTS TABLE
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=True)
    surname = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    reg_no = Column(String(50), unique=True, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    enrollments = relationship("Enrollment", back_populates="student")
    fees = relationship("Fee", back_populates="student")


# 6. ENROLLMENTS TABLE
class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    enrolled_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    class_ = relationship("Class", back_populates="enrollments")
    student = relationship("Student", back_populates="enrollments")
    grades = relationship("Grade", back_populates="enrollment")
    attendance = relationship("Attendance", back_populates="enrollment")


# 7. GRADES TABLE
class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    enrollment_id = Column(Integer, ForeignKey("enrollments.id"), nullable=False)
    score = Column(Numeric(5, 2), nullable=False) # Handles decimal scores like 85.50
    grade_letter = Column(String(5), nullable=False)

    # Relationships
    enrollment = relationship("Enrollment", back_populates="grades")


# 8. ATTENDANCE TABLE
class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    enrollment_id = Column(Integer, ForeignKey("enrollments.id"), nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    status = Column(String(50), nullable=False)

    # Relationships
    enrollment = relationship("Enrollment", back_populates="attendance")


# 9. FEES TABLE
class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    amount_due = Column(Numeric(10, 2), nullable=False)
    amount_paid = Column(Numeric(10, 2), default=0.00, nullable=False)
    status = Column(String(50), nullable=False)

    # Relationships
    student = relationship("Student", back_populates="fees")
