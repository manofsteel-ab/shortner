from flask import Blueprint

from app.settings.custom_response import DefaultResponse
urlBp = Blueprint('url', __name__, url_prefix='/url/')


@urlBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})
