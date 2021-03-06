# IMPORTS
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user

from app import db
from models import Student, Teacher, School, Parent, User
from students.forms import StudentRegForm, TeacherRegForm, ParentRegForm, LoginForm
from werkzeug.security import check_password_hash, generate_password_hash

# CONFIG
users_blueprint = Blueprint('students', __name__, template_folder='templates')


# VIEWS
# view registration
@users_blueprint.route('/student_register', methods=['GET', 'POST'])
def student_register():
    # create signup form object
    form = StudentRegForm()

    # if request method is POST or form is valid
    if form.validate_on_submit():
        # if username already exists redirect user back to signup page with error message so user can try again
        user = Student.query.filter_by(Username=form.username.data).first()
        if user:
            flash('Username already exists, go to the login page')
            return render_template('studentRegister.html', form=form)

        # if teacher id doesn't exist, then the user can't register
        teacher = Teacher.query.filter_by(TeacherID=form.teacher_id.data).first()
        if not teacher:
            flash('That Teacher ID does not exist')
            return render_template('studentRegister.html', form=form)

        # if sic doesn't exits, then the user can't register
        sic = School.query.filter_by(SIC=form.sic.data).first()
        if not sic:
            flash('That SIC does not exist')
            return render_template('studentRegister.html', form=form)

        hashed_password = generate_password_hash(form.password.data)

        # create a new user with the form data
        new_user = Student(FirstName=form.firstname.data,
                           LastName=form.lastname.data,
                           SIC=form.sic.data,
                           TeacherID=form.teacher_id.data,
                           Password=hashed_password,
                           Username=form.username.data)

        new_student = User(Username=form.username.data,
                           Password=hashed_password,
                           Role='student')

        # add the new user to the database
        db.session.add(new_user)
        db.session.add(new_student)
        db.session.commit()

        # sends user to login page
        return redirect(url_for('students.login'))
    # if request method is GET or form not valid re-render signup page
    return render_template('studentRegister.html', form=form)


@users_blueprint.route('/parent_register', methods=['GET', 'POST'])
def parent_register():
    form = ParentRegForm()

    if form.validate_on_submit():
        user = Parent.query.filter_by(Email=form.email.data).first()
        if user:
            flash('Email already exists, go to the login page')
            return render_template('parentRegister.html', form=form)

        # if sic doesn't exits, then the user can't register
        sic = School.query.filter_by(SIC=form.sic.data).first()
        if not sic:
            flash('That SIC does not exist')
            return render_template('parentRegister.html', form=form)

        # if student id doesn't exits, then the user can't register
        student_id = Student.query.filter_by(StudentID=form.student_id.data).first()
        if not student_id:
            flash('That Student does not exist')
            return render_template('parentRegister.html', form=form)

        hashed_password = generate_password_hash(form.password.data)

        # create a new user with the form data
        new_user = Parent(FirstName=form.firstname.data,
                          LastName=form.lastname.data,
                          SIC=form.sic.data,
                          StudentID=form.student_id.data,
                          Email=form.email.data,
                          Password=hashed_password)

        new_parent = User(Username=form.email.data,
                          Password=hashed_password,
                          Role='parent')

        # add the new user to the database
        db.session.add(new_user)
        db.session.add(new_parent)
        db.session.commit()

        return redirect(url_for('students.login'))
    return render_template('parentRegister.html', form=form)


@users_blueprint.route('/teacher_register', methods=['GET', 'POST'])
def teacher_register():
    form = TeacherRegForm()

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

        hashed_password = generate_password_hash(form.password.data)

        # create a new user with the form data
        new_user = Teacher(FirstName=form.firstname.data,
                           LastName=form.lastname.data,
                           SIC=form.sic.data,
                           Password=hashed_password,
                           Email=form.email.data)

        new_teacher = User(Username=form.email.data,
                           Password=hashed_password,
                           Role='teacher')

        # add the new user to the database
        db.session.add(new_user)
        db.session.add(new_teacher)
        db.session.commit()

        return redirect(url_for('students.login'))
    return render_template('teacherRegister.html', form=form)


# Login page
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # Redirect the user to an unauthorised notice!
        return render_template('403.html')

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(Username=form.username.data).first()

        if not user or not check_password_hash(user.Password, form.password.data):
            flash('Please check your login details and try again')
            return render_template('login.html', form=form)
        login_user(user)

        return account()
    return render_template('login.html', form=form)


# view accounts page
@users_blueprint.route('/account')
@login_required
def account():
    if current_user.Role == 'student':
        user = Student.query.filter_by(Username=current_user.Username).first()
        usertype = 'Username'
        username = user.Username
    elif current_user.Role == 'teacher':
        user = Teacher.query.filter_by(Email=current_user.Username).first()
        usertype = 'Email'
        username = user.Email
    else:
        user = Parent.query.filter_by(Email=current_user.Username).first()
        usertype = 'Email'
        username = user.Email
    name = user.FirstName + ' ' + user.LastName
    sic = user.SIC
    school = School.query.filter_by(SIC=user.SIC).first()
    school_name = school.SchoolName
    return render_template('account.html', name=name, usernameEmail=usertype,
                           user=username, SIC=sic, schoolName=school_name, role=current_user.Role.capitalize())


# about goal 14 page
@users_blueprint.route('/about')
def about():
    return render_template('about.html')


# home page when not logged in
@users_blueprint.route('/index')
def index():
    return render_template('index.html')


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
