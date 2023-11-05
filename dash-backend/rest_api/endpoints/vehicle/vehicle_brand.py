from flask import Blueprint, request

from actions.vehicle.vehicle_brand import vehicle_brand_action
from actions.vehicle.vehicle_model import vehicle_model_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

vehicle_brand_ctrl = Blueprint(name='vehicle_brand_ctrl', import_name=__name__, url_prefix='/vehicle_brands')


@vehicle_brand_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle_brand = vehicle_brand_action.create(data)

    return SuccessResponse(vehicle_brand, 201)


@vehicle_brand_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_brand_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_brand_ctrl.route('/<int:vehicle_brand_id>/vehicle_models', methods=['GET'])
def get_all_by_vehicle_brand_id(vehicle_brand_id):
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_model_action.get_all_by_vehicle_brand_id(vehicle_brand_id, **request_data)

    return PagingResponse(items, total)


@vehicle_brand_ctrl.route('/<int:vehicle_brand_id>', methods=['GET'])
def get(vehicle_brand_id):
    vehicle_brand = vehicle_brand_action.get(vehicle_brand_id)
    return SuccessResponse(vehicle_brand, 200)


@vehicle_brand_ctrl.route('/<int:vehicle_brand_id>/logo', methods=['POST'])
def update_logo(vehicle_brand_id):
    blob_files = request.files.getlist('VehicleBrandLogo')
    vehicle_brand = vehicle_brand_action.update_logo(vehicle_brand_id, blob_files)

    return SuccessResponse(vehicle_brand, 200)


@vehicle_brand_ctrl.route('/<int:vehicle_brand_id>', methods=['PUT'])
def update(vehicle_brand_id):
    data = request.get_json()

    vehicle_brand = vehicle_brand_action.update(vehicle_brand_id, data)

    return SuccessResponse(vehicle_brand, 200)


@vehicle_brand_ctrl.route('/<int:vehicle_brand_id>', methods=['DELETE'])
def delete(vehicle_brand_id):
    vehicle_brand_action.delete(vehicle_brand_id)
    return SuccessResponse(None, 200)
