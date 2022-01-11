# IMPORTS
import logging
from functools import wraps

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user

from app import db
from models import Student, Teacher, School
from students.forms import RegisterForm, teacherLoginForm, teacherRegForm

# CONFIG
users_blueprint = Blueprint('students', __name__, template_folder='templates')


# VIEWS
# view registration
@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    # create signup form object
    form = RegisterForm()

    # if request method is POST or form is valid
    if form.validate_on_submit():
        # if username already exists redirect user back to signup page with error message so user can try again
        user = Student.query.filter_by(Username=form.username.data).first()
        if user:
            flash('Username already exists, go to the login page')
            return render_template('register.html', form=form)

        # if teacher id doesn't exist, then the user can't register
        teacher = Teacher.query.filter_by(TeacherID=form.teacher_id.data).first()
        if not teacher:
            flash('That Teacher ID does not exist')
            return render_template('register.html', form=form)

        # if sic doesn't exits, then the user can't register
        sic = School.query.filter_by(SIC=form.sic.data).first()
        if not sic:
            flash('That SIC does not exist')
            return render_template('register.html', form=form)

        # create a new user with the form data
        new_user = Student(FirstName=form.firstname.data,
                           LastName=form.lastname.data,
                           SIC=form.sic.data,
                           TeacherID=form.teacher_id.data,
                           Password=form.password.data,
                           Username=form.username.data)

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        # sends user to login page
        return redirect(url_for('students.login'))
    # if request method is GET or form not valid re-render signup page
    return render_template('register.html', form=form)


# register pages
@users_blueprint.route('/studentRegister')
def studentRegister():
    return render_template('studentRegister.html')


@users_blueprint.route('/parentRegister')
def parentRegister():
    return render_template('parentRegister.html')


@users_blueprint.route('/teacherRegister', methods=['GET', 'POST'])
def teacherRegister():
    form = teacherRegForm()

    if form.validate_on_submit():
        user = Teacher.query.filter_by(Email=form.email.data).first()
        if user:
            flash('Email already exists, go to the login page')
            return render_template('teacherRegister.html', form=form)

        # if sic doesn't exits, then the user can't register
        sic = School.query.filter_by(SIC=form.sic.data).first()
        if not sic:
            flash('That SIC does not exist')
            return render_template('teacherRegister.html', form=form)

        # create a new user with the form data
        new_user = Teacher(FirstName=form.firstname.data,
                           LastName=form.lastname.data,
                           SIC=form.sic.data,
                           Password=form.password.data,
                           Email=form.email.data)

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('students.teacherLogin'))
    return render_template('teacherRegister.html', form=form)


# Login pages
@users_blueprint.route('/teacherLogin', methods=['GET', 'POST'])
def teacherLogin():
    form = RegisterForm()
    return render_template('teacherLogin.html', form=form)


@users_blueprint.route('/studentLogin')
def studentLogin():
    return render_template('studentLogin.html')


@users_blueprint.route('/parentLogin')
def parentLogin():
    return render_template('parentLogin.html')


# view turtle game
@users_blueprint.route('/turtleGame')
def turtleGame():
    return render_template('turtleGame.html')


# home page when not logged in
@users_blueprint.route('/index')
def index():
    return render_template('index.html')
