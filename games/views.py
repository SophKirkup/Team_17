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
        score = 0
        game = ""
        success = True



        if "sourceGame" in request.form:
            game = request.form.get("sourceGame")
        else:
            success = False
        if "score" in request.form:
            score = int(request.form.get("score"))
        else:
            success = False
        if "checkSum" in request.form:


            checkSum = float(request.form.get("checkSum"))

            salt1 = 48372000
            salt2 = 16584

            # checksum is calculated  as (((salt1+score)/salt2) x score), so to check, do
            # round((((checkSum/score)*salt2)-salt1)), and it should equal score.
            # this is not perfectly secure, but for a kids website this level of security
            # for high scores is sufficient
            score2 = round((((checkSum/score)*salt2)-salt1))
            if score2==score:
                print(str(score2),"==",str(score),", score IS from",game)
            else:
                print(str(score2),"=/=",str(score),", score IS NOT from",game,". Likely to be cheating attempt.")
                success = False
        else:
            print("no checksum")
            success = False

        if success:
            print("Recieved score from " + game + ", of " + str(score))
        else:
            print("one or more values were incorrect. score not saved.")


    response = {
                  "success": success,
                  "score": score,
                  "game": game
                }
    return response