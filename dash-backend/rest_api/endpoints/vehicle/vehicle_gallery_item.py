from flask import Blueprint, request

from actions.vehicle.vehicle_gallery_item import vehicle_gallery_item_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

vehicle_gallery_item_ctrl = Blueprint(name='vehicle_gallery_item_ctrl', import_name=__name__,
                                      url_prefix='/vehicle_gallery_items')


@vehicle_gallery_item_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle_gallery_item = vehicle_gallery_item_action.create(data)

    return SuccessResponse(vehicle_gallery_item, 201)


@vehicle_gallery_item_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_gallery_item_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_gallery_item_ctrl.route('/<int:vehicle_gallery_item_id>', methods=['GET'])
def get(vehicle_gallery_item_id):
    vehicle_gallery_item = vehicle_gallery_item_action.get(vehicle_gallery_item_id)
    return SuccessResponse(vehicle_gallery_item, 200)


@vehicle_gallery_item_ctrl.route('/<int:vehicle_gallery_item_id>', methods=['PUT'])
def update(vehicle_gallery_item_id):
    data = request.get_json()

    vehicle_gallery_item = vehicle_gallery_item_action.update(vehicle_gallery_item_id, data)

    return SuccessResponse(vehicle_gallery_item, 200)


@vehicle_gallery_item_ctrl.route('/<int:vehicle_gallery_item_id>', methods=['DELETE'])
def delete(vehicle_gallery_item_id):
    vehicle_gallery_item_action.delete(vehicle_gallery_item_id)
    return SuccessResponse(None, 200)
