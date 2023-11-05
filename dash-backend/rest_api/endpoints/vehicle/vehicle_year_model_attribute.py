from flask import Blueprint, request

from actions.vehicle.vehicle_year_model_attribute import vehicle_year_model_attribute_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

vehicle_year_model_attribute_ctrl = Blueprint(name='vehicle_year_model_attribute_ctrl', import_name=__name__,
                                              url_prefix='/vehicle_year_model_attributes')


@vehicle_year_model_attribute_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle_year_model_attribute = vehicle_year_model_attribute_action.create(data)

    return SuccessResponse(vehicle_year_model_attribute, 201)


@vehicle_year_model_attribute_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_year_model_attribute_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_year_model_attribute_ctrl.route('/<int:vehicle_year_model_attribute_id>', methods=['GET'])
def get(vehicle_year_model_attribute_id):
    vehicle_year_model_attribute = vehicle_year_model_attribute_action.get(vehicle_year_model_attribute_id)
    return SuccessResponse(vehicle_year_model_attribute, 200)


@vehicle_year_model_attribute_ctrl.route('/<int:vehicle_year_model_attribute_id>', methods=['PUT'])
def update(vehicle_year_model_attribute_id):
    data = request.get_json()

    vehicle_year_model_attribute = vehicle_year_model_attribute_action.update(vehicle_year_model_attribute_id, data)

    return SuccessResponse(vehicle_year_model_attribute, 200)


@vehicle_year_model_attribute_ctrl.route('/<int:vehicle_year_model_attribute_id>', methods=['DELETE'])
def delete(vehicle_year_model_attribute_id):
    vehicle_year_model_attribute_action.delete(vehicle_year_model_attribute_id)
    return SuccessResponse(None, 200)
