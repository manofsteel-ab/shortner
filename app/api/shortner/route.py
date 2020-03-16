from flask import Blueprint, request, redirect, render_template, abort, flash
from flask_login import login_required, current_user
from app.api.shortner.managers.shortner import ShortnerManager
from app.api.shortner.schemas.url_form import ShortnerForm
from app.settings.custom_response import DefaultResponse
shortnerBP = Blueprint('shortner', __name__, url_prefix='/shortner/')


@shortnerBP.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})


@shortnerBP.route('/index/', methods=['POST', 'GET'])
@login_required
def index():
    form = ShortnerForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        long_url = form.long_url.data
        custom_code = form.custom_code.data
        try:
            short_url = ShortnerManager().get_short_url(long_url, custom_code)
            return render_template(
                'index.html', form=form, short_url=short_url, username=current_user.username or "Anonymous"
            )
        except Exception as e:
            flash(str(e))
            return render_template('index.html', form=form, username=current_user.username or "Anonymous")
    else:
        return render_template('index.html', form=ShortnerForm(), username=current_user.username or "Anonymous")


@shortnerBP.route('/<string:hash_val>/', methods=['GET', 'POST'])
def get_original_url(hash_val):
    long_url = ShortnerManager().get_original_url(hash_val)
    if not long_url:
        abort(404)
    return redirect(long_url)


@shortnerBP.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@shortnerBP.errorhandler(401)
def page_not_found(e):
    return render_template('401.html')
