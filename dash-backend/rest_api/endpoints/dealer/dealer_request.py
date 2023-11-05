from flask import Blueprint, request, g

from actions.dealer.dealer_request import dealer_request_action
from rest_api.decorators import is_authenticated
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

dealer_request_ctrl = Blueprint(name='dealer_request_ctrl', import_name=__name__, url_prefix='/dealer_requests')


@dealer_request_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    dealer_request = dealer_request_action.create(data)

    return SuccessResponse(dealer_request, 201)


@dealer_request_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = dealer_request_action.get_all(**request_data)

    return PagingResponse(items, total)


@dealer_request_ctrl.route('/user', methods=['GET'])
@is_authenticated
def get_all_by_current_user():
    user_id = g.payload['sub']
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = dealer_request_action.get_all_by_current_user(user_id, **request_data)

    return PagingResponse(items, total)


@dealer_request_ctrl.route('/<int:dealer_request_id>', methods=['GET'])
def get(dealer_request_id):
    dealer_request = dealer_request_action.get(dealer_request_id)
    return SuccessResponse(dealer_request, 200)


@dealer_request_ctrl.route('/<int:dealer_request_id>', methods=['PUT'])
def update(dealer_request_id):
    data = request.get_json()

    dealer_request = dealer_request_action.update(dealer_request_id, data)

    return SuccessResponse(dealer_request, 200)


@dealer_request_ctrl.route('/<int:dealer_request_id>', methods=['DELETE'])
def delete(dealer_request_id):
    dealer_request_action.delete(dealer_request_id)
    return SuccessResponse(None, 200)
