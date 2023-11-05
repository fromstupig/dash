from flask import Blueprint, request

from actions.dealer.dealer_scheduler import dealer_scheduler_action
from rest_api.wrapper import PagingResponse, SuccessResponse
from schemas.request import GeneralFilterSchema

dealer_scheduler_ctrl = Blueprint(name='dealer_scheduler_ctrl', import_name=__name__, url_prefix='/dealer_schedulers')


@dealer_scheduler_ctrl.route('', methods=['POST'])
def create():
    data = request.get_json()
    dealer_scheduler = dealer_scheduler_action.create(data)

    return SuccessResponse(dealer_scheduler, 201)


@dealer_scheduler_ctrl.route('', methods=['GET'])
def get_all():
    request_data = GeneralFilterSchema().load(request.args.to_dict())
    items, total = dealer_scheduler_action.get_all(**request_data)

    return PagingResponse(items, total)


@dealer_scheduler_ctrl.route('/<int:dealer_scheduler_id>/month/<int:month_num>', methods=['GET'])
def get_monthly_scheduler_by_dealer(dealer_scheduler_id, month_num):
    items, total = dealer_scheduler_action.get_monthly_scheduler_by_dealer(dealer_scheduler_id, month_num)

    return PagingResponse(items, total)


@dealer_scheduler_ctrl.route('/<int:dealer_scheduler_id>', methods=['GET'])
def get(dealer_scheduler_id):
    dealer_scheduler = dealer_scheduler_action.get(dealer_scheduler_id)
    return SuccessResponse(dealer_scheduler, 200)


@dealer_scheduler_ctrl.route('/<int:dealer_scheduler_id>', methods=['PUT'])
def update(dealer_scheduler_id):
    data = request.get_json()

    dealer_scheduler = dealer_scheduler_action.update(dealer_scheduler_id, data)

    return SuccessResponse(dealer_scheduler, 200)


@dealer_scheduler_ctrl.route('/<int:dealer_scheduler_id>', methods=['DELETE'])
def delete(dealer_scheduler_id):
    dealer_scheduler_action.delete(dealer_scheduler_id)
    return SuccessResponse(None, 200)
