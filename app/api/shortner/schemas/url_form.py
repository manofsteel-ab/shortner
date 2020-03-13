from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import url


class UrlForm(FlaskForm):
    original_url = URLField(validators=[url()])
    custom_code = StringField('custom_code')