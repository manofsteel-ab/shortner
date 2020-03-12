from flask import Blueprint

from app.settings.custom_response import DefaultResponse
zooKeeperBp = Blueprint('zookeeper', __name__, url_prefix='/zooKeeper/')


@zooKeeperBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})