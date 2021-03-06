from http import HTTPStatus
from redis import Redis
from jsonschema import ValidationError, SchemaError

from app.settings.configs import app_config, Config
from app.settings.custom_flask import DefaultFlask

__all__ = ['create_app']

from app.settings.custom_response import DefaultResponse


def create_app(config=None, app_name=None):
    """Create an app instance based on the passed params"""
    if not app_name:
        app_name = Config.APP_NAME
    if not config:
        config = 'default'
    app = DefaultFlask(app_name)
    app = configure_app(app, config)
    app = configure_blueprints(app)
    app = configure_extensions(app)
    app = configure_error_handlers(app)
    app = configure_redis(app)
    return app


def configure_app(app, config=None):
    app.config.from_object(app_config[config])
    return app


def configure_extensions(app):
    from app.settings.extensions import db
    from app.settings.extensions import migrate
    from app.settings.extensions import csrf
    from app.settings.extensions import login_manager
    # from app.settings.extensions import redis
    db.init_app(app)
    # redis.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    # session.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'
    return app


def configure_blueprints(app):
    """Register all blueprints with the app"""
    from app.api import userBp, shortnerBP, zooKeeperBp, analyticBp, healthBp
    for bp in [userBp, shortnerBP, zooKeeperBp, analyticBp, healthBp]:
        app.register_blueprint(bp)
    return app


def configure_error_handlers(app):
    """ Error handler subscribe """

    def handle_custom_api_exception(e):
        return e.to_result()

    def handle_unknown_exception(e):
        return DefaultResponse({}, str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

    app.register_error_handler(Exception, handle_unknown_exception)
    app.register_error_handler(
        ValidationError, lambda err: DefaultResponse(
            {'error': str(err)}, 'Invalid request body', HTTPStatus.BAD_REQUEST
        )
    )
    app.register_error_handler(
        SchemaError, lambda err: DefaultResponse(
            {'error': str(err)}, 'Invalid schema at server',
            HTTPStatus.INTERNAL_SERVER_ERROR
        )
    )
    return app


def configure_redis(app):
    config = app.config
    app.cache = Redis(
        host=config.get('REDIS_HOST'),
        port=config.get('REDIS_PORT'),
        db=config.get('REDIS_CACHE_DB')
    )
    app.rate_limiter = Redis(
        host=config.get('REDIS_HOST'),
        port=config.get('REDIS_PORT'),
        db=config.get('REDIS_RATE_LIMITER_DB')
    )
    return app
