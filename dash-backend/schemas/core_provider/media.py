from marshmallow import fields, EXCLUDE, Schema

from models.core_provider import MediaProvider
from schemas.base import IdSchema, ModificationTimeSchema, CreationTimeSchema


class MediaUploadResponseSchema(Schema):
    public_id = fields.String()
    gallery = fields.String()


media_upload_response_schema = MediaUploadResponseSchema()
media_list_upload_response_schema = MediaUploadResponseSchema(many=True)


class MediaResourceSchema(ModificationTimeSchema, CreationTimeSchema):
    class Meta:
        unknown = EXCLUDE

    public_id = fields.String(required=True)
    format = fields.String(allow_none=True)


media_resource_schema = MediaResourceSchema()
media_resources_schema = MediaResourceSchema(many=True)


class MediaProviderSchema(IdSchema, ModificationTimeSchema, CreationTimeSchema):
    __model__ = MediaProvider

    class Meta:
        unknown = EXCLUDE

    resources = fields.Nested(MediaResourceSchema, many=True)


media_provider_schema = MediaProviderSchema()
media_providers_schema = MediaProviderSchema(many=True)
