from flask import Blueprint, request

from actions.vehicle.vehicle_option_item import vehicle_option_item_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

vehicle_option_item_ctrl = Blueprint(name='vehicle_option_item_ctrl', import_name=__name__,
                                     url_prefix='/vehicle_option_items')


@vehicle_option_item_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle_option_item = vehicle_option_item_action.create(data)

    return SuccessResponse(vehicle_option_item, 201)


@vehicle_option_item_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_option_item_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_option_item_ctrl.route('/<int:vehicle_option_item_id>', methods=['GET'])
def get(vehicle_option_item_id):
    vehicle_option_item = vehicle_option_item_action.get(vehicle_option_item_id)
    return SuccessResponse(vehicle_option_item, 200)


@vehicle_option_item_ctrl.route('/<int:vehicle_option_item_id>/avatar', methods=['POST'])
def update_avatar(vehicle_option_item_id):
    blob_files = request.files.getlist('VehicleOptionItemAvatar')
    vehicle_option_item = vehicle_option_item_action.update_avatar(vehicle_option_item_id, blob_files)

    return SuccessResponse(vehicle_option_item, 200)


@vehicle_option_item_ctrl.route('/<int:vehicle_option_item_id>', methods=['PUT'])
def update(vehicle_option_item_id):
    data = request.get_json()

    vehicle_option_item = vehicle_option_item_action.update(vehicle_option_item_id, data)

    return SuccessResponse(vehicle_option_item, 200)


@vehicle_option_item_ctrl.route('/<int:vehicle_option_item_id>', methods=['DELETE'])
def delete(vehicle_option_item_id):
    vehicle_option_item_action.delete(vehicle_option_item_id)
    return SuccessResponse(None, 200)
