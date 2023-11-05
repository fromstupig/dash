from flask import Blueprint, request

from actions.authorization.role import role_action
from rest_api.decorators import is_authenticated, is_authorized
from rest_api.wrapper import SuccessResponse
from schemas.authorization.role import role_schema, role_schemas

role_ctrl = Blueprint(name='role_ctrl', import_name=__name__, url_prefix='/roles')


@role_ctrl.route('', methods=['POST'])
@is_authenticated
@is_authorized(['RoleManagement.Create'])
def create():
    data = request.get_json()
    validate_data = role_schema.load(data)
    role = role_action.create(validate_data)
    result = role_schema.dump(role)

    return SuccessResponse(result, 200)


@role_ctrl.route('/', methods=['GET'])
@is_authenticated
@is_authorized(['RoleManagement.GetAll'])
def get_all():
    roles = role_action.get_all()
    result = role_schemas.dump(roles)

    return SuccessResponse(result, 200)


@role_ctrl.route('/<role_id>/permissions', methods=['POST'])
@is_authenticated
@is_authorized(['RoleManagement.Update'])
def update_permissions(role_id):
    data = request.get_json()
    role = role_action.update_permissions(role_id=role_id, data=data)
    result = role_schema.dump(role)

    return SuccessResponse(result, 200)


@role_ctrl.route('/<role_id>', methods=['DELETE'])
@is_authenticated
@is_authorized(['RoleManagement.Delete'])
def delete(role_id):
    role_action.delete(role_id)

    return SuccessResponse(None, 200)
