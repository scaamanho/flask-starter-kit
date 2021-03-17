"""
    flask configuration found in http://flask.pocoo.org/docs/0.12/config/
"""


class BaseConfig:
    HOST = "0.0.0.0"
    PORT = 8000
    ADMINS = frozenset(['amdmin@example.com'])
    SECRET_KEY = 'SecretKeyForSessionSigning'
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "somethingimpossibletoguess"


class ProductionConfig(BaseConfig):
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
