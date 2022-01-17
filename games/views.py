from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from app import db, requires_roles
from models import Student, School

games_blueprint = Blueprint('games', __name__, template_folder='templates')


# view turtle game
@games_blueprint.route('/turtle_game')
@login_required
@requires_roles('student')
def turtle_game():
    return render_template('turtleGame.html')


# view pollution game
@games_blueprint.route('/pollution_game')
@login_required
@requires_roles('student')
def pollution_game():
    return render_template('pollutionGame.html')


@games_blueprint.route('/submitScore', methods=['POST'])
def submit_score():
    if request.method == 'POST':
        score = 1
        game = "No Game Specified"
        success = True
        errors = []

        if "sourceGame" in request.form:
            game = request.form.get("sourceGame")

            # source game names
            # kieran's game - TurtleGame
            # charlie's game - PollutionGame
        else:
            success = False
            errors.append("noSourceGame")
        if "score" in request.form:
            score = int(round(float(request.form.get("score"))))
        else:
            success = False
            errors.append("noScore")
        if "checkSum" in request.form:

            check_sum = float(request.form.get("checkSum"))

            # key values for checksum, same values are hard coded into each game's scoring scripts.
            s1 = 541
            s2 = 225

            # checksum is calculated  as ((s1+score)*s2)*s1), so to check, do
            # ((check_sum/s1)/s2)-s1), and it should equal score.
            # this is not very secure, but for a kids website this level of security
            # for high scores is sufficient, and will make it at least tamper proof
            score2 = round(((check_sum / s1) / s2) - s1)
            if not score2 == score:
                success = False
                score = -1
                errors.append("checksumFalse")
        else:
            success = False
            errors.append("noCheckSum")

        if not current_user.is_authenticated:
            success = False
            errors.append("noUserLoggedIn")

        if success:
            print("Received score from " + game + ", of " + str(score), ", is legitimate.")

            # put code here for saving a correct score from the game
            save_score(score)

        else:
            print("Received score from " + game + ", of " + str(score),
                  "but with Errors: [" + ", ".join(errors)+"]. Score will not be saved.")

    response = {
        "errors": errors,
        "success": success,
        "score": score,
        "game": game
    }
    return response


def save_score(score):
    if current_user.is_authenticated:
        if current_user.Role == 'student':
            # update user's score
            user = Student.query.filter_by(Username=current_user.Username).first()
            previous_score = user.Points
            new_score = previous_score + score
            user.Points = new_score

            # update the schools total score
            users_school = School.query.filter_by(SIC=user.SIC).first()
            school_old_score = users_school.TotalPoints
            new_school_score = school_old_score + score
            users_school.TotalPoints = new_school_score

            db.session.commit()
        else:
            print("Score can only be saved if you are a student")
    else:
        print("No user logged in, score not saved.")
