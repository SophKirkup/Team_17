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
        game = "GameName"
        success = True

        print(request.form)

        if "sourceGame" in request.form:
            game = request.form.get("sourceGame")
        else:
            success = False
        if "score" in request.form:
            score = request.form.get("score")
        else:
            success = False
        print("Recieved score from "+game+", of "+str(score))

    response = {
                  "success": success,
                  "score": score,
                  "game": game
                }
    return response