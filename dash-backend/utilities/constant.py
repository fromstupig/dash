import ipaddress
import os

from flask import current_app

DEFAULT_LANGUAGE = 'en'
DEFAULT_CURRENCY = 'USD'
QUERY_SEPARATE_SYMBOL = '+'
CONDITION_SEPARATE_SYMBOL = '='
VALUE_SEPARATE_SYMBOL = ','
ORDER_SEPARATE_SYMBOL = '+'
HOURS_SEPARATE_SYMBOL = '-'
DIRECTION_SEPARATE_SYMBOL = ':'
PASSWORD_ENCODING = 'utf8'
FULLTEXT_SEARCH_BIG_NUMBER = 10000


def default_password():
    return current_app.config['DEFAULT_PASSWORD']


def root_dir():
    return current_app.config['ROOT_DIR']


def machine_id():
    instance_ip = ipaddress.IPv4Address(os.environ.get('INSTANCE_PRIVATE_ID') or '127.0.0.1')
    _, digit2, digit3, _ = instance_ip.__str__().split('.')
    return int(digit2) << 8 | int(digit3)


def config_env():
    return os.environ.get('FLASK_ENV') or 'development'


def get_s3_bucket():
    return current_app.config['S3_BUCKET']


def get_s3_key():
    return current_app.config['S3_KEY']


def get_s3_secret():
    return current_app.config['S3_SECRET']


def get_s3_location():
    return current_app.config['S3_LOCATION']
