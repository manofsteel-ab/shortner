from app.settings.configs import app_config, Config
from app.settings.custom_flask import DefaultFlask

__all__ = ['create_app']


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
    return app


def configure_app(app, config=None):
    app.config.from_object(app_config[config])
    return app


def configure_extensions(app):
    from app.settings.extensions import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)
    return app


def configure_blueprints(app):
    """Register all blueprints with the app"""
    from app.api.users import userBp
    from app.api.shortner import urlBp
    for bp in [userBp, urlBp]:
        app.register_blueprint(bp)
    return app


def configure_error_handlers(app):
    """ Error handler subscribe """
    return app
