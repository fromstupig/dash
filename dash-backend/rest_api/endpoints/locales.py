from flask import Blueprint, request

from actions.core_provider.locale import locale_action
from rest_api.decorators import allow_anonymous
from rest_api.wrapper import SuccessResponse
from schemas.core_provider.locale import locales_schema

locale_ctrl = Blueprint(name='locale_ctrl', import_name=__name__, url_prefix='/locales/')


@locale_ctrl.route('', methods=['GET'])
@allow_anonymous
def get_all():
    is_active = request.args.get('is_active', True)
    locales = locale_action.get_all(is_active)

    return SuccessResponse(locales_schema.dump(locales), 200)
