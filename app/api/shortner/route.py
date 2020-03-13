from flask import Blueprint, request

from app.api.shortner.managers.url import UrlManager
from app.api.shortner.schemas.create_short_url import CreateShortUrlSchema
from app.commons.utils import validate_request_schema
from app.settings.custom_response import DefaultResponse
urlBp = Blueprint('url', __name__, url_prefix='/url/')


@urlBp.route('health/', methods=['GET'])
def app_health():
    return DefaultResponse(data={})


@urlBp.route('/', methods=['POST'])
@validate_request_schema(schema=CreateShortUrlSchema)
def index():
    payload = request.json
    short_url = UrlManager().get_short_url(
        long_url=payload.get('longUrl')
    )
    return DefaultResponse(
        data={
            'shortUrl': short_url
        }
    )


@urlBp.route('/<string:hash_val>/', methods=['GET'])
def get_original_url(hash_val):
    long_url = UrlManager().get_original_url(hash_val)
    return DefaultResponse(
        data={
            "longUrl": long_url
        }
    )
