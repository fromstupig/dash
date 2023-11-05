from flask import Blueprint, request

from actions.vehicle.vehicle_history import vehicle_history_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

vehicle_history_ctrl = Blueprint(name='vehicle_history_ctrl', import_name=__name__, url_prefix='/vehicle_historys')


@vehicle_history_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle_history = vehicle_history_action.create(data)

    return SuccessResponse(vehicle_history, 201)


@vehicle_history_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_history_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_history_ctrl.route('/<int:vehicle_history_id>', methods=['GET'])
def get(vehicle_history_id):
    vehicle_history = vehicle_history_action.get(vehicle_history_id)
    return SuccessResponse(vehicle_history, 200)


@vehicle_history_ctrl.route('/<int:vehicle_history_id>', methods=['PUT'])
def update(vehicle_history_id):
    data = request.get_json()

    vehicle_history = vehicle_history_action.update(vehicle_history_id, data)

    return SuccessResponse(vehicle_history, 200)


@vehicle_history_ctrl.route('/<int:vehicle_history_id>', methods=['DELETE'])
def delete(vehicle_history_id):
    vehicle_history_action.delete(vehicle_history_id)
    return SuccessResponse(None, 200)
