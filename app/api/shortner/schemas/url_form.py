from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import URLField
from wtforms.validators import url, Length


class ShortnerForm(FlaskForm):
    long_url = URLField(validators=[url()])
    custom_code = StringField('custom_code')
