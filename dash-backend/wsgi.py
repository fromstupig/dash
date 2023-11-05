import json

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import request, Response, g, url_for, Blueprint
from flask_compress import Compress
from marshmallow import ValidationError

import actions
import models
import rest_api
import services
import schemas

from factory import create_app
from utilities.constant import config_env, DEFAULT_LANGUAGE, DEFAULT_CURRENCY
from utilities.exception import EntityNotFoundException, DuplicateException, ForbiddenException, \
    BadRequestException, UnauthorizedException, MissingFieldException, InternalServerException, \
    InvalidRefreshTokenException
from utilities.helper import Utility

compress = Compress()

app = create_app(__name__, config_env())


def enum_to_properties(self, field, **kwargs):
    """
    Add an OpenAPI extension for marshmallow_enum.EnumField instances
    """
    import marshmallow_enum
    if isinstance(field, marshmallow_enum.EnumField):
        return {'type': 'string', 'enum': [m.name for m in field.enum]}
    return {}


marshmallow_plugin = MarshmallowPlugin()

spec = APISpec(
    title="Swagger Petstore",
    version="1.0.0",
    openapi_version="2.0.0",
    plugins=[marshmallow_plugin],
)

marshmallow_plugin.converter.add_attribute_function(enum_to_properties)

compress.init_app(app)
schemas.init_app(app, spec)
rest_api.init_app(app, spec)
services.init_app(app, models.db)
actions.init_app(app)


@app.route('/', methods=['GET'])
def health_check():
    return Response(json.dumps({'message': 'OK'}), mimetype='application/json', status=200)


@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return handle_exception(BadRequestException(detail={**e.messages}))


@app.errorhandler(UnauthorizedException)
@app.errorhandler(ForbiddenException)
@app.errorhandler(BadRequestException)
@app.errorhandler(MissingFieldException)
@app.errorhandler(EntityNotFoundException)
@app.errorhandler(DuplicateException)
@app.errorhandler(InternalServerException)
@app.errorhandler(InvalidRefreshTokenException)
def handle_exception(e):
    return Response(json.dumps(e.to_dict()),  mimetype='application/json', status=e.status_code)


@app.before_request
def before_request():
    header_format = '{}-{}'
    prefix = app.config['HEADER_PREFIX']
    g.language = request.headers.get(header_format.format(prefix, 'Language'), DEFAULT_LANGUAGE)
    g.currency = request.headers.get(header_format.format(prefix, 'Currency'), DEFAULT_CURRENCY)

    all_language = request.headers.get(header_format.format(prefix, 'All-Language'), False)
    g.all_language = Utility.safe_bool(all_language)

    all_currency = request.headers.get(header_format.format(prefix, 'All-Currency'), False)
    g.all_currency = Utility.safe_bool(all_currency)


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = \
            'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers

    return response

