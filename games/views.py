from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user


games_blueprint = Blueprint('games', __name__, template_folder='templates')

# view turtle game
@games_blueprint.route('/turtleGame')
def turtleGame():
    return render_template('turtleGame.html')

# view pollution game
@games_blueprint.route('/pollutionGame')
def pollutionGame():
    return render_template('pollutionGame.html')


@games_blueprint.route('/submitScore', methods = ['POST'])
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
            score2 = round(((checkSum/s1)/s2)-s1)
            if not score2==score:
                success = False
                score = -1
                errors.append("checksumFalse")
        else:
            success = False
            errors.append("noCheckSum")

        if success:
            print("Recieved score from " + game + ", of " + str(score),", is legitimate.")

            # put code here for saving a correct score from the game

        else:
            print("Recieved score from " + game + ", of " + str(score), ", is illegitimate.")



    response = {
                  "errors": errors,
                  "success": success,
                  "score": score,
                  "game": game
                }
    return response