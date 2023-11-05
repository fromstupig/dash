from flask import Blueprint, request

from actions.vehicle.vehicle_feature import vehicle_feature_action
from rest_api.wrapper import PagingResponse
from schemas.request import GeneralFilterSchema

vehicle_feature_ctrl = Blueprint(name='vehicle_feature_ctrl', import_name=__name__, url_prefix='/vehicles_features')


@vehicle_feature_ctrl.route('/engines', methods=['GET'])
def get_all_engine():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_feature_action.get_all_engine(**request_data)

    return PagingResponse(items, total)


@vehicle_feature_ctrl.route('/bodies', methods=['GET'])
def get_all_body():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_feature_action.get_all_body(**request_data)

    return PagingResponse(items, total)


@vehicle_feature_ctrl.route('/drive_trains', methods=['GET'])
def get_all_drive_train():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_feature_action.get_all_drive_train(**request_data)

    return PagingResponse(items, total)


@vehicle_feature_ctrl.route('/transmissions', methods=['GET'])
def get_all_transmission():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = vehicle_feature_action.get_all_transmission(**request_data)

    return PagingResponse(items, total)
