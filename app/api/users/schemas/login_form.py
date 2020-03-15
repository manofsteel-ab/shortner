from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError


class LoginForm(FlaskForm):
    username = TextField('Username', validators=[DataRequired(), Length(4, 14)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 14)])
    submit = SubmitField('Log In')
