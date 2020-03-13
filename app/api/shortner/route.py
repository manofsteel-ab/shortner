from flask import Blueprint, request, redirect, render_template, abort, flash

from app.api.shortner.managers.url import UrlManager
from app.api.shortner.schemas.url_form import UrlForm
from app.settings.custom_response import DefaultResponse
urlBp = Blueprint('url', __name__, url_prefix='/url')


@urlBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})


@urlBp.route('/', methods=['POST', 'GET'])
def index():
    form = UrlForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        original_url = form.original_url.data
        custom_code = form.custom_code.data
        try:
            short_url = UrlManager().get_short_url(original_url, custom_code)
            return render_template('index.html', form=form, short_url=short_url)
        except Exception as e:
            flash(str(e))
            return render_template('index.html', form=form)
    else:
        return render_template('index.html', form=UrlForm())


@urlBp.route('/<string:hash_val>/', methods=['GET'])
def get_original_url(hash_val):
    long_url = UrlManager().get_original_url(hash_val)
    if not long_url:
        abort(404)
    return redirect(long_url)


@urlBp.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
