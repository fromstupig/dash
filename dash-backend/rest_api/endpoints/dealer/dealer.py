from flask import Blueprint, request

from actions.dealer.dealer import dealer_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

dealer_ctrl = Blueprint(name='dealer_ctrl', import_name=__name__, url_prefix='/dealers')


@dealer_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    dealer = dealer_action.create(data)

    return SuccessResponse(dealer, 201)


@dealer_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = dealer_action.get_all(**request_data)

    return PagingResponse(items, total)


@dealer_ctrl.route('/<int:dealer_id>', methods=['GET'])
def get(dealer_id):
    dealer = dealer_action.get(dealer_id)
    return SuccessResponse(dealer, 200)


@dealer_ctrl.route('/<int:dealer_id>', methods=['PUT'])
def update(dealer_id):
    data = request.get_json()

    dealer = dealer_action.update(dealer_id, data)

    return SuccessResponse(dealer, 200)


@dealer_ctrl.route('/<int:dealer_id>', methods=['DELETE'])
def delete(dealer_id):
    dealer_action.delete(dealer_id)
    return SuccessResponse(None, 200)
