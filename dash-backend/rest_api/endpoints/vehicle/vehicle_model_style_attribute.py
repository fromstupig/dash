from flask import Blueprint, request

from actions.vehicle.vehicle_model_style_attribute import vehicle_model_style_attribute_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

vehicle_model_style_attribute_ctrl = Blueprint(name='vehicle_model_style_attribute_ctrl', import_name=__name__,
                                               url_prefix='/vehicle_model_style_attributes')


@vehicle_model_style_attribute_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle_model_style_attribute = vehicle_model_style_attribute_action.create(data)

    return SuccessResponse(vehicle_model_style_attribute, 201)


@vehicle_model_style_attribute_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_model_style_attribute_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_model_style_attribute_ctrl.route('/<int:vehicle_model_style_attribute_id>', methods=['GET'])
def get(vehicle_model_style_attribute_id):
    vehicle_model_style_attribute = vehicle_model_style_attribute_action.get(vehicle_model_style_attribute_id)
    return SuccessResponse(vehicle_model_style_attribute, 200)


@vehicle_model_style_attribute_ctrl.route('/<int:vehicle_model_style_attribute_id>', methods=['PUT'])
def update(vehicle_model_style_attribute_id):
    data = request.get_json()

    vehicle_model_style_attribute = vehicle_model_style_attribute_action.update(vehicle_model_style_attribute_id, data)

    return SuccessResponse(vehicle_model_style_attribute, 200)


@vehicle_model_style_attribute_ctrl.route('/<int:vehicle_model_style_attribute_id>', methods=['DELETE'])
def delete(vehicle_model_style_attribute_id):
    vehicle_model_style_attribute_action.delete(vehicle_model_style_attribute_id)
    return SuccessResponse(None, 200)
