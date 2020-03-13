from flask import Blueprint, request, redirect, render_template, abort

from app.api.shortner.managers.url import UrlManager
from app.api.shortner.schemas.url_form import UrlForm
from app.settings.custom_response import DefaultResponse
urlBp = Blueprint('url', __name__, url_prefix='/url/')


@urlBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})


@urlBp.route('', methods=['POST', 'GET'])
def index():
    form = UrlForm(request.form)
    if request.method == 'POST' and form.validate():
        long_url = form.originalUrl.data
        custom_code = form.shortCode.data
        return render_template('success.html')
    else:
        return render_template('index.html', title='Home', form=form)


@urlBp.route('/<string:hash_val>/', methods=['GET'])
def get_original_url(hash_val):
    long_url = UrlManager().get_original_url(hash_val)
    if not long_url:
        abort(404)
    return redirect(long_url)


@urlBp.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
