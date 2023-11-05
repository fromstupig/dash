from flask import Blueprint, request

from actions.vehicle.vehicle_model_style import vehicle_model_style_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema, SearchSchema

vehicle_model_style_ctrl = Blueprint(name='vehicle_model_style_ctrl', import_name=__name__,
                                     url_prefix='/vehicle_model_styles')


@vehicle_model_style_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle_model_style = vehicle_model_style_action.create(data)

    return SuccessResponse(vehicle_model_style, 201)


@vehicle_model_style_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_model_style_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_model_style_ctrl.route('/<int:vehicle_model_style_id>', methods=['GET'])
def get(vehicle_model_style_id):
    vehicle_model_style = vehicle_model_style_action.get(vehicle_model_style_id)
    return SuccessResponse(vehicle_model_style, 200)


@vehicle_model_style_ctrl.route('/<int:vehicle_model_style_id>/avatar', methods=['POST'])
def update_avatar(vehicle_model_style_id):
    blob_files = request.files
    vehicle_model_style = vehicle_model_style_action.update_avatar(vehicle_model_style_id, blob_files)

    return SuccessResponse(vehicle_model_style, 200)


@vehicle_model_style_ctrl.route('/<int:vehicle_model_style_id>/cover', methods=['POST'])
def update_cover(vehicle_model_style_id):
    blob_files = request.files
    vehicle_model_style = vehicle_model_style_action.update_cover(vehicle_model_style_id, blob_files)

    return SuccessResponse(vehicle_model_style, 200)


@vehicle_model_style_ctrl.route('/<int:vehicle_model_style_id>/introduction_video', methods=['POST'])
def update_introduction_video(vehicle_model_style_id):
    blob_files = request.files
    vehicle_model_style = vehicle_model_style_action.update_introduction_video(vehicle_model_style_id,
                                                                               blob_files)

    return SuccessResponse(vehicle_model_style, 200)


@vehicle_model_style_ctrl.route('/<int:vehicle_model_style_id>', methods=['PUT'])
def update(vehicle_model_style_id):
    data = request.get_json()

    vehicle_model_style = vehicle_model_style_action.update(vehicle_model_style_id, data)

    return SuccessResponse(vehicle_model_style, 200)


@vehicle_model_style_ctrl.route('/<int:vehicle_model_style_id>', methods=['DELETE'])
def delete(vehicle_model_style_id):
    vehicle_model_style_action.delete(vehicle_model_style_id)
    return SuccessResponse(None, 200)


@vehicle_model_style_ctrl.route('/<int:vehicle_model_style_id>/attribute_values', methods=['POST'])
def update_attribute_values(vehicle_model_style_id):
    data = request.get_json()
    vehicle_model_style = vehicle_model_style_action.update_attribute_values(vehicle_model_style_id,
                                                                             data, True)

    return SuccessResponse(vehicle_model_style, 200)


@vehicle_model_style_ctrl.route('/_search', methods=['GET'])
def search():
    request_data = SearchSchema().load(request.args.to_dict())
    search_result = vehicle_model_style_action.search(request_data)

    return SuccessResponse(search_result, 200)
