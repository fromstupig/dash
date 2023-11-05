from flask import Blueprint, request
from actions.core_provider.media import media_action
from rest_api.decorators import is_authenticated
from rest_api.wrapper import SuccessResponse, PagingResponse
from schemas.request import MediaPaginationSchema

media_ctrl = Blueprint(name='media_ctrl', import_name=__name__, url_prefix='/media')


@media_ctrl.route('/', methods=['POST'])
def upload():
    gallery = request.args.get('gallery')
    blob_files = request.files.getlist('file')
    file_links = request.form.getlist('file')
    media = media_action.upload(gallery, blob_files + file_links)
    return SuccessResponse(media, 201)


@media_ctrl.route('/', methods=['DELETE'])
def remove():
    public_id = request.args.get('public_id')
    media_action.remove_resource(public_id)
    return SuccessResponse(None, 200)


@media_ctrl.route('/_tag', methods=['PUT'])
def tag():
    data = request.get_json()
    response = media_action.tag(data['public_ids'], data['tag'])
    return SuccessResponse(response, 200)


@media_ctrl.route('/_remove_tag', methods=['PUT'])
def remove_tag():
    data = request.get_json()
    media_action.remove_tag(data['public_ids'], data['tag'])
    return SuccessResponse(None, 200)


@media_ctrl.route('/', methods=['GET'])
@is_authenticated
def find_all():
    pagination = MediaPaginationSchema().load({
        'page': request.args.get('page', 1, int),
        'limit': request.args.get('limit', 10, int),
    })
    total, tags = media_action.get_all_media(**pagination)
    return PagingResponse(tags, total)
