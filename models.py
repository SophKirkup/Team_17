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


class Teacher(db.Model, UserMixin):
    __tablename__ = 'Teachers'

    TeacherID = db.Column(db.Integer, primary_key=True)

    SIC = db.Column(db.String(20), nullable=False)
    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(100), nullable=False)

    def __init__(self, SIC, FirstName, LastName, Email, Password):
        self.SIC = SIC
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Password = Password


class School(db.Model, UserMixin):
    __tablename__ = 'Schools'

    SIC = db.Column(db.String(20), primary_key=True)

    SchoolName = db.Column(db.String(100), nullable=False)
    TotalPoints = db.Column(db.Integer, nullable=True)

    def __init__(self, SchoolName):
        self.SchoolName = SchoolName
        self.TotalPoints = None


class Parent(db.Model, UserMixin):
    __tablename__ = 'Parents'

    ParentID = db.Column(db.Integer, primary_key=True)

    FirstName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    SIC = db.Column(db.String(20), nullable=False)
    StudentID = db.Column(db.Integer, nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(100), nullable=False)

    def __init__(self, FirstName, LastName, SIC, StudentID, Email, Password):
        self.FirstName = FirstName
        self.LastName = LastName
        self.SIC = SIC
        self.StudentID = StudentID
        self. Email = Email
        self.Password = Password


class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)

    Username = db.Column(db.String(20), nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    Role = db.Column(db.String(100), nullable=False)

    def __init__(self, Username, Password, Role):
        self.Username = Username
        self.Password = Password
        self.Role = Role
