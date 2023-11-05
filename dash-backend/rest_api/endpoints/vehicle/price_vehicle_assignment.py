from flask import Blueprint, request

from actions.vehicle.price_vehicle_assignment import price_vehicle_assignment_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

price_vehicle_assignment_ctrl = Blueprint(name='price_vehicle_assignment_ctrl', import_name=__name__,
                                          url_prefix='/price_vehicle_assignments')


@price_vehicle_assignment_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    price_vehicle_assignment = price_vehicle_assignment_action.create(data)

    return SuccessResponse(price_vehicle_assignment, 201)


@price_vehicle_assignment_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = price_vehicle_assignment_action.get_all(**request_data)

    return PagingResponse(items, total)


@price_vehicle_assignment_ctrl.route('/<int:price_vehicle_assignment_id>', methods=['GET'])
def get(price_vehicle_assignment_id):
    price_vehicle_assignment = price_vehicle_assignment_action.get(price_vehicle_assignment_id)
    return SuccessResponse(price_vehicle_assignment, 200)


@price_vehicle_assignment_ctrl.route('/<int:price_vehicle_assignment_id>', methods=['PUT'])
def update(price_vehicle_assignment_id):
    data = request.get_json()

    price_vehicle_assignment = price_vehicle_assignment_action.update(price_vehicle_assignment_id, data)

    return SuccessResponse(price_vehicle_assignment, 200)


@price_vehicle_assignment_ctrl.route('/<int:price_vehicle_assignment_id>', methods=['DELETE'])
def delete(price_vehicle_assignment_id):
    price_vehicle_assignment_action.delete(price_vehicle_assignment_id)
    return SuccessResponse(None, 200)
