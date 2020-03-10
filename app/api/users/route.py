from flask import Blueprint

from app.settings.custom_response import DefaultResponse
userBp = Blueprint('user', __name__, url_prefix='/user/')


@userBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})
