# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# reate an engine
engine = create_engine("sqlite:///groups.db", echo=True)

# Create a session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# class for creating a table
Base = declarative_base()

class Tutors(Base):
    __tablename__ = "Tutors"
    tutor_id = Column(Integer, primary_key=True)
    name = Column(String)

class Groups(Base):
    __tablename__ = "Groups"
    group_id = Column(Integer, primary_key=True)
    group_name = Column(String)

class Students(Base):
    __tablename__ = "Students"
    student_id = Column(Integer, primary_key=True)
    student_name = Column(String)
    group_id = Column(Integer, ForeignKey("Groups.group_id"))

class Subjects(Base):
    __tablename__ = "Subjects"
    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String)
    tutor_id = Column(Integer, ForeignKey("Tutors.tutor_id"))

class Marks(Base):
    __tablename__ = "Marks"
    mark_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("Students.student_id"))
    subject_id = Column(Integer, ForeignKey("Subjects.subject_id"))
    mark = Column(Integer)
    time = Column(DATETIME)

# Create the tables
Base.metadata.create_all(engine)
Base.metadata.bind = engine

