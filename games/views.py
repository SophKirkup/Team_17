from flask import Blueprint, render_template, flash, redirect, url_for, request, send_from_directory
from flask_login import current_user
from app import db
from models import Student, School

games_blueprint = Blueprint('games', __name__, template_folder='templates')


# view turtle game
@games_blueprint.route('/turtleGame')
def turtleGame():
    return render_template('turtleGame.html')


# view pollution game
@games_blueprint.route('/pollutionGame')
def pollutionGame():
    return render_template('pollutionGame.html')


@games_blueprint.route('/submitScore', methods=['POST'])
def submitScore():
    if request.method == 'POST':
        score = 1
        game = "No Game"
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
            score = int(request.form.get("score"))
        else:
            success = False
            errors.append("noScore")
        if "checkSum" in request.form:

            checkSum = float(request.form.get("checkSum"))

            # key values for checksum, same values are hard coded into each game's scoring scripts.
            s1 = 541
            s2 = 225

            # checksum is calculated  as ((s1+score)*s2)*s1), so to check, do
            # ((checkSum/s1)/s2)-s1), and it should equal score.
            # this is not very secure, but for a kids website this level of security
            # for high scores is sufficient, and will make it at least tamper proof
            score2 = round(((checkSum / s1) / s2) - s1)
            if not score2 == score:
                success = False
                score = -1
                errors.append("checksumFalse")
        else:
            success = False
            errors.append("noCheckSum")

        if success:
            print("Recieved score from " + game + ", of " + str(score), ", is legitimate.")

            # put code here for saving a correct score from the game
            saveScore(score)

        else:
            print("Recieved score from " + game + ", of " + str(score), ", is illegitimate.")

    response = {
        "errors": errors,
        "success": success,
        "score": score,
        "game": game
    }
    return response


def saveScore(score):
    if current_user.Role == 'student':
        #update user's score
        user = Student.query.filter_by(Username=current_user.Username).first()
        previousScore = user.Points
        newScore = previousScore + score
        user.Points = newScore

        #update the schools total score
        usersSchool = School.query.filter_by(SIC=user.SIC).first()
        schoolOldScore = usersSchool.TotalPoints
        newSchoolScore = schoolOldScore + score
        usersSchool.TotalPoints = newSchoolScore


        db.session.commit()
    else:
        print("Score can only be saved if you are a student")
