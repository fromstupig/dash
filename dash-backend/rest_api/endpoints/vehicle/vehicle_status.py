from flask import Blueprint, request

from actions.vehicle.vehicle_status import vehicle_status_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

vehicle_status_ctrl = Blueprint(name='vehicle_status_ctrl', import_name=__name__, url_prefix='/vehicle_statuss')


@vehicle_status_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle_status = vehicle_status_action.create(data)

    return SuccessResponse(vehicle_status, 201)


@vehicle_status_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_status_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_status_ctrl.route('/<int:vehicle_status_id>', methods=['GET'])
def get(vehicle_status_id):
    vehicle_status = vehicle_status_action.get(vehicle_status_id)
    return SuccessResponse(vehicle_status, 200)


@vehicle_status_ctrl.route('/<int:vehicle_status_id>', methods=['PUT'])
def update(vehicle_status_id):
    data = request.get_json()

    vehicle_status = vehicle_status_action.update(vehicle_status_id, data)

    return SuccessResponse(vehicle_status, 200)


@vehicle_status_ctrl.route('/<int:vehicle_status_id>', methods=['DELETE'])
def delete(vehicle_status_id):
    vehicle_status_action.delete(vehicle_status_id)
    return SuccessResponse(None, 200)
