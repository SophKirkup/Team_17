# IMPORTS
import socket
from functools import wraps
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

# CONFIG
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://csc2033_team17:Bat[RiceDeer' \
                                        '@localhost:3500/csc2033_team17'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'

# change StaticPort to False to dynamically assign port, if you are having trouble
# accessing the website on the uni network.
# !! However this will mean scores from games cannot be saved !!
StaticPort = True

# initialise database
db = SQLAlchemy(app)


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.Role not in roles:
                # Redirect the user to an unauthorised notice!
                return render_template('403.html')
            return f(*args, **kwargs)
        return wrapped
    return wrapper


# HOME PAGE VIEW
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def leaderboard():
    return render_template('leaderboard.html')


# ERROR PAGE VIEWS
@app.errorhandler(403)
def page_forbidden(error):
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == "__main__":

    if not StaticPort:
        my_host = "127.0.0.1"
        free_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        free_socket.bind((my_host, 0))
        free_socket.listen(5)
        free_port = free_socket.getsockname()[1]
        free_socket.close()

    login_manager = LoginManager()
    login_manager.login_view = 'students.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(int(uid))

    # BLUEPRINTS
    # import blueprints
    from students.views import users_blueprint
    from games.views import games_blueprint
    from leaderboard.views import lb_blueprint
    from parents.views import parent_blueprint
    from teachers.views import teacher_blueprint

    # register blueprints with app
    app.register_blueprint(users_blueprint)
    app.register_blueprint(games_blueprint)
    app.register_blueprint(lb_blueprint)
    app.register_blueprint(parent_blueprint)
    app.register_blueprint(teacher_blueprint)

    if StaticPort:
        app.run(debug=True)
    else:
        app.run(host=my_host, port=free_port, debug=True)
