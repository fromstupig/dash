from flask import Blueprint, request

from actions.core_provider.address import state_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

state_ctrl = Blueprint(name='state_ctrl', import_name=__name__, url_prefix='/states')


@state_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = state_action.get_all(**request_data)

    return PagingResponse(items, total)


@state_ctrl.route('/<int:country_id>', methods=['GET'])
def get_all_by_country_id(country_id):
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = state_action.get_all_by_country_id(country_id, **request_data)

    return PagingResponse(items, total)
