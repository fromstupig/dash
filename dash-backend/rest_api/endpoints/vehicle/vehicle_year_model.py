from flask import Blueprint, request

from actions.vehicle.vehicle_model_style import vehicle_model_style_action
from actions.vehicle.vehicle_year_model import vehicle_year_model_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

vehicle_year_model_ctrl = Blueprint(name='vehicle_year_model_ctrl', import_name=__name__,
                                    url_prefix='/vehicle_year_models')


@vehicle_year_model_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    vehicle_year_model = vehicle_year_model_action.create(data)

    return SuccessResponse(vehicle_year_model, 201)


@vehicle_year_model_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_year_model_action.get_all(**request_data)

    return PagingResponse(items, total)


@vehicle_year_model_ctrl.route('/<int:vehicle_year_model_id>/vehicle_model_styles', methods=['GET'])
def get_all_model_styles_by_vehicle_year_model_id(vehicle_year_model_id):
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_model_style_action.get_all_model_styles_by_vehicle_year_model_id(vehicle_year_model_id,
                                                                                            **request_data)

    return PagingResponse(items, total)


@vehicle_year_model_ctrl.route('/<int:vehicle_year_model_id>', methods=['GET'])
def get(vehicle_year_model_id):
    vehicle_year_model = vehicle_year_model_action.get(vehicle_year_model_id)
    return SuccessResponse(vehicle_year_model, 200)


@vehicle_year_model_ctrl.route('/<int:vehicle_year_model_id>/avatar', methods=['POST'])
def update_avatar(vehicle_year_model_id):
    blob_files = request.files
    vehicle_year_model = vehicle_year_model_action.update_avatar(vehicle_year_model_id, blob_files)

    return SuccessResponse(vehicle_year_model, 200)


@vehicle_year_model_ctrl.route('/<int:vehicle_year_model_id>/cover', methods=['POST'])
def update_cover(vehicle_year_model_id):
    blob_files = request.files
    vehicle_year_model = vehicle_year_model_action.update_cover(vehicle_year_model_id, blob_files)

    return SuccessResponse(vehicle_year_model, 200)


@vehicle_year_model_ctrl.route('/<int:vehicle_year_model_id>/introduction_video', methods=['POST'])
def update_introduction_video(vehicle_year_model_id):
    blob_files = request.files
    vehicle_year_model = vehicle_year_model_action.update_introduction_video(vehicle_year_model_id,
                                                                             blob_files)

    return SuccessResponse(vehicle_year_model, 200)


@vehicle_year_model_ctrl.route('/<int:vehicle_year_model_id>/exterior', methods=['POST'])
def update_exterior(vehicle_year_model_id):
    blob_files = request.files
    vehicle_year_model = vehicle_year_model_action.update_exterior(vehicle_year_model_id,
                                                                   blob_files)

    return SuccessResponse(vehicle_year_model, 200)


@vehicle_year_model_ctrl.route('/<int:vehicle_year_model_id>/interior', methods=['POST'])
def update_interior(vehicle_year_model_id):
    blob_files = request.files
    vehicle_year_model = vehicle_year_model_action.update_interior(vehicle_year_model_id,
                                                                   blob_files)

    return SuccessResponse(vehicle_year_model, 200)


@vehicle_year_model_ctrl.route('/<int:vehicle_year_model_id>', methods=['PUT'])
def update(vehicle_year_model_id):
    data = request.get_json()

    vehicle_year_model = vehicle_year_model_action.update(vehicle_year_model_id, data)

    return SuccessResponse(vehicle_year_model, 200)


@vehicle_year_model_ctrl.route('/<int:vehicle_year_model_id>', methods=['DELETE'])
def delete(vehicle_year_model_id):
    vehicle_year_model_action.delete(vehicle_year_model_id)
    return SuccessResponse(None, 200)


@vehicle_year_model_ctrl.route('/<int:vehicle_year_model_id>/attribute_values', methods=['POST'])
def update_attribute_values(vehicle_year_model_id):
    data = request.get_json()
    vehicle_year_model = vehicle_year_model_action.update_attribute_values(vehicle_year_model_id,
                                                                           data, True)
    return SuccessResponse(vehicle_year_model, 200)
