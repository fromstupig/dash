import os

import sentry_sdk
from dotenv import load_dotenv
from sentry_sdk.integrations.flask import FlaskIntegration

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    HEADER_PREFIX = 'dash'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:HelloDash1234@dash-dev.cgi0zstuigrj.us-east-1.rds.amazonaws.com/dash'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_ECHO = False

    ES_HOST = os.environ.get('ES_HOST') or 'localhost'
    ES_PORT = int(os.environ.get('ES_PORT', '9200'))
    ES_USE_SSL = os.environ.get('ES_USE_SSL', 'FALSE') == 'TRUE'
    ES_USER = os.environ.get('ES_USER', '')
    ES_PASSWORD = os.environ.get('ES_PASSWORD', '')

    JWT_SECRET = os.environ.get('JWT_SECRET') or 'you-never-guess'
    JWT_EXPIRE = os.environ.get('JWT_EXPIRE') or 86400 * 10

    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY') or 'you-never-guess'

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 587
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or True
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'info.dash@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'you-nerver-guest'
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    DEFAULT_PASSWORD = os.environ.get('DEFAULT_PASSWORD') or 'Hello@Dash+1234'

    COMPRESS_MIMETYPES = ['application/json']
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500

    FACEBOOK_ACCESS_TOKEN = os.environ.get('FACEBOOK_ACCESS_TOKEN') or 'you-never-guess'

    EVOX_API_URL = os.environ.get('EVOX_API_URL') or ' http://api.evoximages.com/api/v1'
    EVOX_API_KEY = os.environ.get('EVOX_API_KEY') or 'PGLMEYbeQqywrTDrPyyFXsDusAs35RS4'

    DS_TOKEN = os.environ.get('DS_TOKEN') or '2eljiAqjTyGDNMODYI0h7w=='
    DS_URL = os.environ.get('DS_URL') or 'https://api.dealerscience.com/vehicles/deals'

    SCHEDULER_DEFAULT_MAX_SESSION = 2
    SCHEDULER_DEFAULT_TIMESPAN = 30  # minutes

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SWAGGER = {'uiversion': 3}
    API_DOCS = os.environ.get('API_DOCS')


class ProductionConfig(Config):
    DEBUG = False
    API_DOCS = os.environ.get('API_DOCS')
    SWAGGER = {'uiversion': 3}

    SENTRY_DSN = os.environ.get('SENTRY_DSN')
    SENTRY_ENV = os.environ.get('SENTRY_ENV')

    @staticmethod
    def init_app(app):
        Config.init_app(app)
        sentry_sdk.init(dsn=app.config['SENTRY_DSN'], environment=app.config['SENTRY_ENV'],
                        integrations=[FlaskIntegration()])


class MigrationConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'migration': MigrationConfig
}
