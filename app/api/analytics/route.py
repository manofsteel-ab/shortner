from flask import Blueprint
from app.settings.custom_response import DefaultResponse
analyticBp = Blueprint('analytics', __name__, url_prefix='/api/analytics/')


@analyticBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})
