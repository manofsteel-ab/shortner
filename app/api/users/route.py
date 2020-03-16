from flask import Blueprint, request, redirect, url_for, render_template, flash, current_app
from flask_login import login_user, logout_user, login_required
from app.api.users.managers.user import UserManager
from app.api.users.schemas.login_form import LoginForm
from app.api.users.schemas.registration_form import RegistrationForm
from app.commons.utils.constants import UserType
from app.settings.custom_response import DefaultResponse
from app.settings.extensions import login_manager

userBp = Blueprint('users', __name__, url_prefix='/users')


@userBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})


@userBp.route('/register/', methods=['POST', 'GET'])
def register():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        try:
            data = {
                "username": form.username.data,
                "password": form.password.data,
                "email": form.email.data,
                "primary_phone": form.primary_phone.data,
                "first_name": form.first_name.data,
                "middle_name": form.middle_name.data,
                "last_name": form.last_name.data,
                'user_roles': [UserType.NON_SYSTEM]
            }
            user = UserManager().register_user(user_attributes=data)
            next_page = UserManager().fetch_user_default_page(user_id=user.id)
            login_user(user)
            return redirect(url_for(next_page))
        except Exception as e:
            flash(str(e))
            return render_template('registration.html', form=form)
    return render_template('registration.html', form=RegistrationForm())


@userBp.route('/create_demo_user/', methods=['POST', 'GET'])
def register_demo_user():
    payload = {
        "username": "test_demo_user",
        "password": "test_demo_user",
        "email": "test_demo_user@mailinator.com",
        "user_roles": ["non_system"]
    }
    UserManager().register_user(user_attributes=payload)
    return DefaultResponse(
        data={
            'username': payload.get('username'),
            'password': payload.get('password')
        }, status=201, message='created'
    )


@userBp.route('/create_admin_user/<string:secret_key>/', methods=['POST', 'GET'])
def register_admin_user(secret_key):
    if not secret_key or secret_key != current_app.config['SECRET_KEY']:
        raise Exception("Permission denied")
    payload = {
        "username": "test_admin_user",
        "password": "test_admin_user",
        "email": "test_admin_user@mailinator.com",
        "user_roles": ["system"]
    }
    try:
        UserManager().register_user(user_attributes=payload)
    except Exception as e:
        print(str(e))
    return DefaultResponse(
        data={
            'username': payload.get('username'),
            'password': payload.get('password')
        }, status=201, message='created'
    )


@userBp.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        try:
            user = UserManager().log_me_in(
                username=form.username.data,
                password=form.password.data
            )
            next_page = UserManager().fetch_user_default_page(user_id=user.id)
            login_user(user)
            return redirect(url_for(next_page))
        except Exception as e:
            flash(str(e))
            return render_template('login.html', form=form)
    return render_template('login.html', form=LoginForm())


@userBp.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("users.login"))


# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    return UserManager().fetch_user(user_id=user_id)
