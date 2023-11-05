from flask import Blueprint, request

from actions.vehicle.vehicle_attribute_value import vehicle_attribute_value_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

vehicle_attribute_value_ctrl = Blueprint(name='vehicle_attribute_value_ctrl', import_name=__name__,
                                         url_prefix='/vehicle_attribute_values')


@vehicle_attribute_value_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle_attribute_value = vehicle_attribute_value_action.create(data)

    return SuccessResponse(vehicle_attribute_value, 201)


@vehicle_attribute_value_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_attribute_value_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_attribute_value_ctrl.route('/<int:vehicle_attribute_value_id>', methods=['GET'])
def get(vehicle_attribute_value_id):
    vehicle_attribute_value = vehicle_attribute_value_action.get(vehicle_attribute_value_id)
    return SuccessResponse(vehicle_attribute_value, 200)


@vehicle_attribute_value_ctrl.route('/<int:vehicle_attribute_value_id>', methods=['PUT'])
def update(vehicle_attribute_value_id):
    data = request.get_json()

    vehicle_attribute_value = vehicle_attribute_value_action.update(vehicle_attribute_value_id, data)

    return SuccessResponse(vehicle_attribute_value, 200)


@vehicle_attribute_value_ctrl.route('/<int:vehicle_attribute_value_id>', methods=['DELETE'])
def delete(vehicle_attribute_value_id):
    vehicle_attribute_value_action.delete(vehicle_attribute_value_id)
    return SuccessResponse(None, 200)
