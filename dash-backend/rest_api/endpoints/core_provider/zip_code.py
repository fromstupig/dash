from flask import Blueprint

from actions.core_provider.address import zip_code_action

zip_code_ctrl = Blueprint(name='zip_code_ctrl', import_name=__name__, url_prefix='/zip_codes')


@zip_code_ctrl.route('/<int:zip_code>', methods=['GET'])
def get_by_zip_code(zip_code):
    item = zip_code_action.get_by_zip_code(zip_code)

    return item
