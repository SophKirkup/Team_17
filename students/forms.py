import re
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import Length, EqualTo, ValidationError, Email
from wtforms.validators import InputRequired as Required


class studentRegForm(FlaskForm):
    username = StringField(validators=[Required()])
    firstname = StringField(validators=[Required()])
    lastname = StringField(validators=[Required()])
    password = PasswordField(validators=[Required(), Length(min=5, max=15,
                                                            message="Password must be between 5  and 15 characters "
                                                                    "long.")])
    confirm_password = PasswordField(validators=[Required(), EqualTo('password', message="Both passwords must match.")])
    teacher_id = StringField(validators=[Required()])
    sic = StringField(validators=[Required()])
    submit = SubmitField()

    def validate_firstname(self, firstname):
        f = re.compile(r"^[a-zA-Z ,.'-]+$")
        if not f.match(self.firstname.data):
            raise ValidationError('First name cannot contain non-name characters')

    def validate_lastname(self, lastname):
        f = re.compile(r"^[a-zA-Z ,.'-]+$")
        if not f.match(self.lastname.data):
            raise ValidationError('Last name cannot contain non-name characters')

    def validate_teacher_id(self, teacher_id):
        f = re.compile(r"^[0-9]+$")
        if not f.match(self.teacher_id.data):
            raise ValidationError('Teacher ID must be a number')

    def validate_sic(self, sic):
        f = re.compile(r"^\s*([A-Za-z]\s*){3}$")
        if not f.match(self.sic.data):
            raise ValidationError('SIC must be a 3 digit character')


class teacherRegForm(FlaskForm):
    sic = StringField(validators=[Required()])
    firstname = StringField(validators=[Required()])
    lastname = StringField(validators=[Required()])
    password = PasswordField(validators=[Required(), Length(min=5, max=15,
                                                            message="Password must be between 5  and 15 characters "
                                                                    "long.")])
    confirm_password = PasswordField(validators=[Required(), EqualTo('password', message="Both passwords must match.")])

    email = StringField(validators=[Required(), Email()])
    submit = SubmitField()

    def validate_firstname(self, firstname):  # check to see if firstname is required
        f = re.compile(r"^[a-zA-Z ,.'-]+$")
        if not f.match(self.firstname.data):
            raise ValidationError('First name cannot contain non-name characters')

    def validate_lastname(self, lastname):
        f = re.compile(r"^[a-zA-Z ,.'-]+$")
        if not f.match(self.lastname.data):
            raise ValidationError('Last name cannot contain non-name characters')

    def validate_sic(self, sic):
        f = re.compile(r"^\s*([A-Za-z]\s*){3}$")
        if not f.match(self.sic.data):
            raise ValidationError('SIC must be a 3 digit character')


class parentRegForm(FlaskForm):
    firstname = StringField(validators=[Required()])
    lastname = StringField(validators=[Required()])
    email = StringField(validators=[Required(), Email()])
    password = PasswordField(validators=[Required(), Length(min=5, max=15,
                                                            message="Password must be between 5  and 15 characters "
                                                                    "long.")])
    confirm_password = PasswordField(validators=[Required(), EqualTo('password', message="Both passwords must match.")])
    sic = StringField(validators=[Required()])
    student_id = StringField(validators=[Required()])
    submit = SubmitField()

    def validate_firstname(self, firstname):  # check to see if firstname is required
        f = re.compile(r"^[a-zA-Z ,.'-]+$")
        if not f.match(self.firstname.data):
            raise ValidationError('First name cannot contain non-name characters')

    def validate_lastname(self, lastname):
        f = re.compile(r"^[a-zA-Z ,.'-]+$")
        if not f.match(self.lastname.data):
            raise ValidationError('Last name cannot contain non-name characters')

    def validate_sic(self, sic):
        f = re.compile(r"^\s*([A-Za-z]\s*){3}$")
        if not f.match(self.sic.data):
            raise ValidationError('SIC must be a 3 digit character')

    def validate_student_id(self, student_id):
        f = re.compile(r"^[0-9]+$")
        if not f.match(self.student_id.data):
            raise ValidationError('Student ID must be a number')


class LoginForm(FlaskForm):
    username = StringField(validators=[Required()])
    password = PasswordField(validators=[Required()])
    submit = SubmitField()


class ResetPasswordForm(FlaskForm):
    student_id = StringField(validators=[Required()])
    password = PasswordField(validators=[Required(), Length(min=5, max=15,
                                                            message="Password must be between 5 and 15 characters "
                                                                    "long.")])
    confirm_password = PasswordField(validators=[Required(), EqualTo('password', message="Both passwords must match.")])
    submit = SubmitField()
