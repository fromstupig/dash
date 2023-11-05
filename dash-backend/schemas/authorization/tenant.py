from marshmallow import EXCLUDE, fields

from models.authorization import Tenant
from schemas.base import DistributeIdSchema


class TenantSchema(DistributeIdSchema):
    __model__ = Tenant

    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True)
    name_url = fields.String(required=True)


tenant_update_schema_fields = ['name']
tenant_schema = TenantSchema()
tenant_update_schema = TenantSchema(include=tenant_update_schema_fields)
tenant_schemas = TenantSchema(many=True)
