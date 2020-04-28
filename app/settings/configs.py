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
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '<$asdhajhdkjahdjahsjkdhajskhdjkashdjkahkjsdhashjdsaj>'
    SHORT_URL = "http://0.0.0.0:8001/shortner/{}/"
    BCRYPT_ROUNDS = 4
    WTF_CSRF_ENABLED = True
    REDIS_HOST = "redis"
    REDIS_PORT = 6379
    REDIS_CACHE_DB = 0
    REDIS_RATE_LIMITER_DB = 1


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
