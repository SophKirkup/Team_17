from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField


class RegisterForm(FlaskForm):
    username = StringField()
    firstname = StringField()
    lastname = StringField()
    password = PasswordField()
    confirm_password = PasswordField()
    teacher_id = StringField()
    sic = StringField()
    submit = SubmitField()
