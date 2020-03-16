from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, SubmitField, TextField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms.fields.html5 import EmailField


class RegistrationForm(FlaskForm):
    username = TextField('Username', validators=[DataRequired(), Length(4, 14)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 14)])
    first_name = StringField('First name')
    middle_name = StringField('Middle name')
    last_name = StringField('Last name')
    email = EmailField('Email', validators=[DataRequired()])
    primary_phone = StringField('Mobile')
    submit = SubmitField('Register')
