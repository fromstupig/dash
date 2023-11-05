from flask import Blueprint, request

from actions.core_provider.address import city_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

city_ctrl = Blueprint(name='city_ctrl', import_name=__name__, url_prefix='/cities')


@city_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = city_action.get_all(**request_data)

    return PagingResponse(items, total)


@city_ctrl.route('/<int:state_id>', methods=['GET'])
def get_all_by_state_id(state_id):
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = city_action.get_all_by_state_id(state_id, **request_data)

    return PagingResponse(items, total)
