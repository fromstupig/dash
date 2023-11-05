from flask import Blueprint, request

from actions.vehicle.vehicle_model import vehicle_model_action
from actions.vehicle.vehicle_year_model import vehicle_year_model_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

vehicle_model_ctrl = Blueprint(name='vehicle_model_ctrl', import_name=__name__, url_prefix='/vehicle_models')


@vehicle_model_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle_model = vehicle_model_action.create(data)

    return SuccessResponse(vehicle_model, 201)


@vehicle_model_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_model_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_model_ctrl.route('/<int:vehicle_model_id>/vehicle_year_models/', methods=['GET'])
def get_all_by_vehicle_model_id(vehicle_model_id):
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_year_model_action.get_all_by_vehicle_model_id(vehicle_model_id, **request_data)

    return PagingResponse(items, total)


@vehicle_model_ctrl.route('/<int:vehicle_model_id>', methods=['GET'])
def get(vehicle_model_id):
    vehicle_model = vehicle_model_action.get(vehicle_model_id)
    return SuccessResponse(vehicle_model, 200)


@vehicle_model_ctrl.route('/<int:vehicle_model_id>/avatar', methods=['POST'])
def update_avatar(vehicle_model_id):
    blob_files = request.files.getlist('VehicleModelAvatar')
    vehicle_model = vehicle_model_action.update_avatar(vehicle_model_id, blob_files)

    return SuccessResponse(vehicle_model, 200)


@vehicle_model_ctrl.route('/<int:vehicle_model_id>', methods=['PUT'])
def update(vehicle_model_id):
    data = request.get_json()

    vehicle_model = vehicle_model_action.update(vehicle_model_id, data)

    return SuccessResponse(vehicle_model, 200)


@vehicle_model_ctrl.route('/<int:vehicle_model_id>', methods=['DELETE'])
def delete(vehicle_model_id):
    vehicle_model_action.delete(vehicle_model_id)
    return SuccessResponse(None, 200)
