from datetime import datetime
from flask_login import UserMixin
from app import db


class Student(db.Model, UserMixin):
    __tablename__ = 'Students'

    StudentID = db.Column(db.Integer, primary_key=True)

    FirstName = db.Column(db.String(100), nullable=False)
    LastName = db.Column(db.String(100), nullable=False)
    Points = db.Column(db.String(100), nullable=True)
    TeacherID = db.Column(db.String(100), nullable=False)
    SIC = db.Column(db.Integer, nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    Username = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, FirstName, LastName, TeacherID, SIC, Password, Username):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Points = None
        self.TeacherID = TeacherID
        self.SIC = SIC
        self.Password = Password
        self.Username = Username
