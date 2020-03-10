class Config:
    """Common configurations"""
    APP_NAME = 'app'


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DB_HOST = "mysql"
    DB_NAME = "shortner"
    DB_USER = "root"
    DB_PASS = ""
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(
        DB_USER, DB_PASS, DB_HOST, DB_NAME
    )
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False


app_config = {
    'default': Config,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
