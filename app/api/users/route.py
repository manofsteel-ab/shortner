from flask import Blueprint

from app.settings.custom_response import DefaultResponse
userBp = Blueprint('custom_auth', __name__, url_prefix='/api/')


@userBp.route('health', methods=['GET'])
def app_health():
    return DefaultResponse(data={})
