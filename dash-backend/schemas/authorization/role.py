from marshmallow import EXCLUDE, fields

from schemas.authorization.permission import PermissionSchema
from schemas.base import IdSchema


class RoleSchema(IdSchema):
    class Meta:
        unknown = EXCLUDE

    name = fields.String(required=True)
    description = fields.String()
    display_name = fields.String()

    permissions = fields.Nested(PermissionSchema, many=True)


role_schema = RoleSchema()
role_schemas = RoleSchema(many=True)
