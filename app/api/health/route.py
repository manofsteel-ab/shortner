from flask import Blueprint, redirect, url_for

healthBp = Blueprint('health', __name__, url_prefix='')


@healthBp.route('/', methods=['GET','POST'])
def app_health():
    return redirect(url_for("users.login"))
