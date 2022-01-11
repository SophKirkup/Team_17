from flask import *

from models import Student, Teacher, School

# config
lb_blueprint = Blueprint('students', __name__, template_folder='templates')


@lb_blueprint.route('/leaderboard')
def leaderboard():
    try:
        students = Student.query.order_by(Student.Points).all()
        student_text = '<ul>'
        for student in students:
            student_text += '<li>' + student.name + ', ' + student.points + '</li>'
        student_text += '</ul>'
        return student_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
