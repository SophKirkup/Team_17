# IMPORTS
import logging
from functools import wraps

from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user

from app import db
from models import Student
from students.forms import RegisterForm

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
        user = Student.query.filter_by(Username=form.username.data).first()
        # if this returns a user, then the email already exists in database

        # if email already exists redirect user back to signup page with error message so user can try again
        if user:
            flash('Username already exists')
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

@users_blueprint.route('/teacherRegister')
def teacherRegister():
    return render_template('teacherRegister.html')


# Login pages
@users_blueprint.route('/studentLogin')
def studentLogin():
    return render_template('studentLogin.html')

@users_blueprint.route('/teacherLogin')
def teacherLogin():
    return render_template('teacherLogin.html')

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