from flask import Blueprint, request

from actions.core_provider.address import country_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

country_ctrl = Blueprint(name='country_ctrl', import_name=__name__, url_prefix='/countries')


@country_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = country_action.get_all(**request_data)

    return PagingResponse(items, total)
