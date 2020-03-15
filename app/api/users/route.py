from flask import Blueprint, request, redirect, url_for, render_template
from app.api.users.managers.user import UserManager
from app.api.users.schemas.login_form import LoginForm
from app.api.users.schemas.register_user_schema import RegisterUserSchema
from app.commons.utils import validate_request_schema
from app.settings.custom_response import DefaultResponse
userBp = Blueprint('users', __name__, url_prefix='/api/users/')


@userBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})


@userBp.route('', methods=['POST'])
@validate_request_schema(schema=RegisterUserSchema)
def register_user():
    payload = request.json
    r = UserManager().register_user(user_attributes=payload).to_dict()
    return DefaultResponse(
        data=r, status=201, message='created'
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
            print(user)
            # login_user(user)
        except Exception as e:
            print(e)
    return render_template('login.html', form=LoginForm())
