from app import requires_roles
from flask import Blueprint, render_template
from flask_login import current_user, login_required
from models import Student, Parent, School, Teacher

# CONFIG
parent_blueprint = Blueprint('parents', __name__, template_folder='templates')


# VIEWS
# parentViewStudent: displays the page which tells the parent about their child
@parent_blueprint.route('/parentViewStudent')
@login_required
@requires_roles('parent')
def parent_view_student():
    parent = Parent.query.filter_by(Email=current_user.Username).first()
    student = Student.query.filter_by(StudentID=parent.StudentID).first()

    school = School.query.filter_by(SIC=student.SIC).first()
    teacher = Teacher.query.filter_by(TeacherID=student.TeacherID).first()
    return render_template('parentViewStudent.html',
                           student=student, school=school, teacher=teacher)
