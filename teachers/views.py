from app import requires_roles, db
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_required
from models import Student, Teacher, User
from students.forms import ResetPasswordForm
from werkzeug.security import check_password_hash, generate_password_hash

# CONFIG
teacher_blueprint = Blueprint('teachers', __name__, template_folder='templates')


# VIEWS
# teacher_view_school: lets a teacher account view all students from that school
@teacher_blueprint.route('/teacherViewSchool')
@login_required
@requires_roles('teacher')
def teacher_view_school():
    teacher = Teacher.query.filter_by(Email=current_user.Username).first()
    students = Student.query.filter_by(SIC=teacher.SIC).all()

    return render_template('teacherViewSchool.html',
                           Students=students)


# reset_password: allows a teacher account to reset a password for a student from their school
@teacher_blueprint.route('/resetPassword', methods=['GET', 'POST'])
@login_required
@requires_roles('teacher')
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # gets the student that matches the Student ID input in the form
        student_to_change = Student.query.filter_by(StudentID=form.student_id.data).first()
        if not student_to_change:  # if the student doesn't exist
            flash("This student doesn't exist, or doesn't go to your school. Please try again")
            return render_template('reset_password.html', form=form)

        # gets the current user's (must be a teacher) email address, for use in the if statement
        current_teacher = Teacher.query.filter_by(Email=current_user.Username).first()
        if student_to_change.SIC != current_teacher.SIC:  # if the student and teacher's schools don't match
            flash("This student doesn't exist, or doesn't go to your school. Please try again")
            return render_template('reset_password.html', form=form)

        # gets the record in the 'Users' table, which is the way the program manages logins
        user_to_change = User.query.filter_by(Username=student_to_change.Username).first()

        hashedPassword = generate_password_hash(form.password.data)

        # updates both records, one in either table, and commits the change to the database
        student_to_change.Password = hashedPassword
        user_to_change.Password = hashedPassword
        db.session.commit()

        return redirect(url_for('teachers.teacher_view_school'))

    return render_template('reset_password.html', form=form)
