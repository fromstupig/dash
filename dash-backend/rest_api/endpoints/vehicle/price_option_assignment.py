from flask import Blueprint, request

from actions.vehicle.price_option_assignment import price_option_assignment_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

price_option_assignment_ctrl = Blueprint(name='price_option_assignment_ctrl', import_name=__name__,
                                         url_prefix='/price_option_assignments')


@price_option_assignment_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    price_option_assignment = price_option_assignment_action.create(data)

    return SuccessResponse(price_option_assignment, 201)


@price_option_assignment_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = price_option_assignment_action.get_all(**request_data)

    return PagingResponse(items, total)


@price_option_assignment_ctrl.route('/<int:price_option_assignment_id>', methods=['GET'])
def get(price_option_assignment_id):
    price_option_assignment = price_option_assignment_action.get(price_option_assignment_id)
    return SuccessResponse(price_option_assignment, 200)


@price_option_assignment_ctrl.route('/<int:price_option_assignment_id>', methods=['PUT'])
def update(price_option_assignment_id):
    data = request.get_json()

    price_option_assignment = price_option_assignment_action.update(price_option_assignment_id, data)

    return SuccessResponse(price_option_assignment, 200)


@price_option_assignment_ctrl.route('/<int:price_option_assignment_id>', methods=['DELETE'])
def delete(price_option_assignment_id):
    price_option_assignment_action.delete(price_option_assignment_id)
    return SuccessResponse(None, 200)
