from flask import Blueprint, request

from actions.vehicle.vehicle import vehicle_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema, SearchSchema

vehicle_ctrl = Blueprint(name='vehicle_ctrl', import_name=__name__, url_prefix='/vehicles')


@vehicle_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle = vehicle_action.create(data)

    return SuccessResponse(vehicle, 201)


@vehicle_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_ctrl.route('/<int:vehicle_id>', methods=['GET'])
def get(vehicle_id):
    vehicle = vehicle_action.get(vehicle_id)
    return SuccessResponse(vehicle, 200)


@vehicle_ctrl.route('/<int:vehicle_id>/avatar', methods=['POST'])
def update_avatar(vehicle_id):
    blob_files = request.files.getlist('VehicleAvatar')
    file_links = request.form.getlist('VehicleAvatar')
    vehicle = vehicle_action.update_avatar(vehicle_id, blob_files + file_links)

    return SuccessResponse(vehicle, 200)


@vehicle_ctrl.route('/<int:vehicle_id>', methods=['PUT'])
def update(vehicle_id):
    data = request.get_json()

    vehicle = vehicle_action.update(vehicle_id, data)

    return SuccessResponse(vehicle, 200)


@vehicle_ctrl.route('/<int:vehicle_id>', methods=['DELETE'])
def delete(vehicle_id):
    vehicle_action.delete(vehicle_id)
    return SuccessResponse(None, 200)


@vehicle_ctrl.route('/_search', methods=['GET'])
def search():
    request_data = SearchSchema().load(request.args.to_dict())
    search_result, total = vehicle_action.search(request_data)

    return PagingResponse(search_result, total)
