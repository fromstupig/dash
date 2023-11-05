from flask import Blueprint, request

from actions.authorization.tenant import tenant_action
from rest_api.decorators import is_authenticated
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

tenant_ctrl = Blueprint(name='tenant_ctrl', import_name=__name__, url_prefix='/countries')


@tenant_ctrl.route('', methods=['POST'])
@is_authenticated
def create():
    data = request.get_json()
    tenant = tenant_action.create(data)

    return SuccessResponse(tenant, 201)


@tenant_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = tenant_action.get_all(**request_data)

    return PagingResponse(items, total)


@tenant_ctrl.route('/<int:tenant_id>', methods=['PUT'])
@is_authenticated
def update(tenant_id):
    data = request.get_json()
    tenant = tenant_action.update(tenant_id, data)

    return SuccessResponse(tenant, 200)


@tenant_ctrl.route('/<int:tenant_id>', methods=['DELETE'])
@is_authenticated
def delete(tenant_id):
    tenant_action.delete(tenant_id)
    return SuccessResponse(None, 200)
