from flask import Blueprint, request, redirect, url_for, render_template

from app.settings.custom_response import DefaultResponse
userBp = Blueprint('user', __name__, url_prefix='/api/users/')


@userBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})


@userBp.route('', methods=['POST'])
def register_user():
    return DefaultResponse(data={})


@userBp.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('shortner.index'))
    return render_template('login.html', error=error)
