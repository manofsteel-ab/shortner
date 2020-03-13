from flask_wtf import FlaskForm  # , RecaptchaField
from wtforms import Form, validators, StringField, SubmitField
from wtforms.validators import Length


class UrlForm(Form):
    originalUrl = StringField('OriginalUrl', [
        validators.InputRequired(),
        validators.Length(
            min=8, max=2000, message="Url length should be greater than 7")
    ])
    shortCode = StringField('shortCode')
    submit = SubmitField('Generate short url')
