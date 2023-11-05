from flask import Blueprint, request, g

from actions.authorization.blacklist_token import blacklist_token_action
from actions.authorization.reset_token import reset_token_action
from actions.authorization.role import ROLE
from actions.authorization.session import session_action
from actions.authorization.user import user_action
from models.authorization.user import User
from rest_api.decorators import is_authenticated
from rest_api.wrapper import SuccessResponse, PagingResponse
from schemas.authorization.user import update_user_schema, user_profile_schema
from schemas.request import GeneralFilterSchema
from services.email import email_service
from services.facebook import facebook_service, FacebookException
from services.google import google_service, GoogleException
from utilities.exception import InvalidRequestException, UnauthorizedException, InvalidRefreshTokenException

auth_ctrl = Blueprint(name='auth_ctrl', import_name=__name__, url_prefix='/authentication')


@auth_ctrl.route('/_register', methods=['POST'])
def register():
    data = request.get_json()
    user = user_action.register(data)
    session = session_action. \
        generate_session(user)
    access_token = session_action.generate_access_token(user)

    return SuccessResponse({
        'access_token': access_token,
        'refresh_token': session.token,
        'user': user_profile_schema.dump(user),
        'impersonate': False
    }, 200)


@auth_ctrl.route('/_add_account', methods=['POST'])
@is_authenticated
def add_account():
    data = request.get_json()
    user = user_action.add_account(data)
    session = session_action.generate_session(user)
    access_token = session_action.generate_access_token(user)

    return SuccessResponse({
        'access_token': access_token,
        'refresh_token': session.token,
        'user': user_profile_schema.dump(user),
        'impersonate': False
    }, 200)


@auth_ctrl.route('/_login', methods=['POST'])
def login():
    data = request.get_json()

    user = user_action.login(data['email'], data['password'])
    if user is None:
        return SuccessResponse(False, 200)

    # if not user.first_login and user.role == ROLE.Admin.value:
    #     result = {
    #         'first_login': user.first_login,
    #         'reset_code': reset_token_action.generate_reset_token(user).token,
    #         'user_email': user.user_email,
    #     }
    # else:
    session = session_action.generate_session(user)
    access_token = session_action.generate_access_token(user, session)
    result = {
        'access_token': access_token,
        'refresh_token': session.token,
        'user': user_profile_schema.dump(user),
        'impersonate': False
    }

    return SuccessResponse(result, 200)


@auth_ctrl.route('/_impersonate', methods=['POST'])
@is_authenticated
def impersonate():
    data = request.get_json()
    impersonate_user_id = g.payload['sub']
    impersonate_as_user_id = data['user_id']

    user = User.query.get(impersonate_as_user_id)
    if user is None:
        return SuccessResponse(False, 200)

    session = session_action.generate_session(user)
    access_token = session_action.generate_access_token(user, session, impersonate_user_id)
    result = {
        'access_token': access_token,
        'refresh_token': session.token,
        'user': user_profile_schema.dump(user),
        'impersonate': True
    }

    return SuccessResponse(result, 200)


@auth_ctrl.route('/_cancel_impersonate', methods=['POST'])
@is_authenticated
def cancel_impersonate():
    payload = g.payload
    if 'custom:impersonate_user_id' not in payload or payload['custom:impersonate_user_id'] is None:
        return SuccessResponse(False, 200)

    impersonate_user_id = payload['custom:impersonate_user_id']
    user = User.query.get(impersonate_user_id)
    if user is None:
        return SuccessResponse(False, 200)

    session = session_action.generate_session(user)
    access_token = session_action.generate_access_token(user, session, impersonate_user_id)
    result = {
        'access_token': access_token,
        'refresh_token': session.token,
        'user': user_profile_schema.dump(user),
        'impersonate': False
    }
    return SuccessResponse(result, 200)


@auth_ctrl.route('/_logout', methods=['POST'])
@is_authenticated
def logout():
    payload = g.payload

    if 'session' in payload:
        session_action.remove_session(payload['custom:session'])

    blacklist_token_action.add(payload['jti'])

    return SuccessResponse({}, 200)


@auth_ctrl.route('/_access_tokens', methods=['POST'])
def generate_access_token():
    try:
        data = request.get_json()
        if ('refresh_token' not in data) or ('user_id' not in data):
            raise UnauthorizedException

        user = User.query.get(data['user_id'])
        if user is None:
            raise UnauthorizedException

        access_token = session_action.regenerate_access_token(data['refresh_token'], user)

        return SuccessResponse({
            'access_token': access_token,
        }, 200)
    except InvalidRefreshTokenException:
        raise UnauthorizedException


@auth_ctrl.route('/_google', methods=['POST'])
def login_with_google():
    try:
        data = request.get_json()
        access_token = ''

        if 'code' in data:
            access_token = google_service.get_access_token(data['code'])
        if 'access_token' in data:
            access_token = data['access_token']
        if 'user_type' in data:
            user_type = data['user_type']

        google_user = google_service.get_logged_in_user(access_token)

        user = User.query.filter_by(google_id=google_user['id']).first()
        if user is None:
            if 'email' not in google_user:
                raise InvalidRequestException(code='NoValidEmail')

            user = User.query.filter_by(user_email=google_user['email']).first()
            if user is None:
                user = user_action.register({
                    'user_email': google_user['email'],
                    'user_full_name': google_user['name'],
                    'google_id': google_user['id'],
                    'type': 1 if user_type is None else user_type,
                    'avatar_url': google_user['picture']
                })
            else:
                user_action.update(user=user, value={'google_id': google_user['id']})

        session = session_action.generate_session(user)
        access_token = session_action.generate_access_token(user, session)

        return SuccessResponse({
            'access_token': access_token,
            'refresh_token': session.token,
            'user': user_profile_schema.dump(user),
        }, 200)
    except GoogleException as e:
        raise InvalidRequestException(e.code)


@auth_ctrl.route('/_facebook', methods=['POST'])
def login_with_facebook():
    try:
        data = request.get_json()

        if 'code' in data:
            access_token = facebook_service.get_access_token(data['code'])
        elif 'access_token' in data:
            access_token = data['access_token']
        else:
            raise InvalidRequestException(
                code='MissingField',
                detail={
                    'message': 'Either "code" or "access_token" is required'
                }
            )

        if 'user_type' in data:
            user_type = data['user_type']

        facebook_user = facebook_service.get_logged_in_user(access_token)

        user = User.query.filter_by(facebook_id=facebook_user['id']).first()
        if user is None:
            if 'email' not in facebook_user:
                raise InvalidRequestException(code='NoValidEmail')

            user = User.query.filter_by(user_email=facebook_user['email']).first()
            if user is None:
                user = user_action.register({
                    'user_email': facebook_user['email'],
                    'user_full_name': facebook_user['name'],
                    'facebook_id': facebook_user['id'],
                    'type': 1 if user_type is None else user_type,
                    'avatar_url': facebook_user['picture']['data']['url']
                })
            else:
                user_action.update(user=user, value={'facebook_id': facebook_user['id']})

        session = session_action.generate_session(user)
        access_token = session_action.generate_access_token(user, session)

        return SuccessResponse({
            'access_token': access_token,
            'refresh_token': session.token,
            'user': user_profile_schema.dump(user)
        }, 200)
    except FacebookException as e:
        raise InvalidRequestException(e.code)


@auth_ctrl.route('/_forgot_password', methods=['POST'])
def forgot_password():
    data = request.get_json()

    user = User.query.filter_by(user_email=data['email']).first()
    if user is None:
        return SuccessResponse({}, 200)  # Return success response to prevent check used email through forgot password

    reset_token = reset_token_action.generate_reset_token(user)
    email_service.send_forgot_password_email(user.user_email, reset_token)

    return SuccessResponse({}, 200)


@auth_ctrl.route('/_reset_code', methods=['POST'])
def check_reset_code():
    data = request.get_json()

    reset_token = reset_token_action.check_reset_token(email=data['email'], token=data['reset_code'])
    if reset_token is None:
        return SuccessResponse(False, 200)

    return SuccessResponse(True, 200)


@auth_ctrl.route('/_reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()

    reset_token = reset_token_action.check_reset_token(email=data['email'], token=data['reset_code'])
    if reset_token is None:
        raise InvalidRequestException(code='NotFound', status_code=404)

    user = User.query.filter_by(user_email=data['email']).first()
    user_action.update(user=user, value={'password': data['password'], 'first_login': True})
    reset_token_action.expired(reset_token)

    return SuccessResponse({}, 200)


@auth_ctrl.route('/_email_exist', methods=['POST'])
def check_email_exist():
    data = request.get_json()

    exist = User.query.filter_by(user_email=data['email']).scalar()
    if exist:
        return SuccessResponse(True, 200)

    return SuccessResponse(False, 200)


@auth_ctrl.route('/admins', methods=['GET'])
@is_authenticated
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = user_action.get_admins(**request_data)

    return PagingResponse(items, total)


@auth_ctrl.route('/users', methods=['GET'])
@is_authenticated
def get_all_users():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = user_action.get_users(**request_data)

    return PagingResponse(items, total)


@auth_ctrl.route('', methods=['PUT'])
@is_authenticated
def update():
    data = request.get_json()
    user = User.query.filter_by(user_email=data['user_email']).first()
    user_action.update(user=user, value={'user_full_name': data['user_full_name']})

    return SuccessResponse({}, 200)


@auth_ctrl.route('/user_profile/<string:email>', methods=['GET'])
@is_authenticated
def get_user_profile(email):
    if email is None:
        user_id = g.payload['sub']
        user = user_action.get(user_id)
    else:
        user = user_action.get_by_email(email)

    if user is not None:
        return SuccessResponse(user, 200)

    return SuccessResponse(None, 200)


@auth_ctrl.route('/user_profile', methods=['PUT'])
@is_authenticated
def update_user_profile():
    data = request.get_json()
    update_user_schema.validate(data)
    user_id = g.payload['sub']
    user_action.update(user_id=user_id, value=data)
    return SuccessResponse({}, 200)
