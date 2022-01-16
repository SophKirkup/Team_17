from flask import *
from sqlalchemy import desc
from models import Student

# config
lb_blueprint = Blueprint('leaderboard', __name__, template_folder='templates')


@lb_blueprint.route('/leaderboard')
def leaderboard():
    try:
        students = Student.query.order_by((desc(Student.Points))).all()
        return render_template('leaderboard.html', Students=students)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
