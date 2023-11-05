from flask import Blueprint, request

from rest_api.wrapper import SuccessResponse
from services import dealer_service

vehicle_payment_ctrl = Blueprint(name='vehicle_payment_ctrl', import_name=__name__,
                                 url_prefix='/vehicles/payments')


@vehicle_payment_ctrl.route('', methods=['POST'])
def get_payment_by_deal():
    rv = dealer_service.get_vehicle_payment_by_deal(request.get_json())
    return SuccessResponse(rv, 200)
