from marshmallow import Schema, fields

from utilities.helper import Utility


class DistributeIdSchema(Schema):
    id = fields.String(allow_none=True, allow_empty=True)


class IdSchema(Schema):
    id = fields.Integer(allow_none=True)


class CreationTimeSchema(Schema):
    creation_date = fields.DateTime(dump_only=True)


class ModificationTimeSchema:
    modification_date = fields.DateTime(dump_only=True)


class PriceAssignmentSchema:
    start_date = fields.DateTime()
    end_date = fields.DateTime()
    value_in_cent = fields.Integer()
    region_id = fields.Integer()


class PassivableSchema(Schema):
    is_active = fields.Boolean()


class SlugableSchema(Schema):
    slug = fields.String()


class I18nNameSchema(Schema):
    name_en = fields.String()
    name_vi = fields.String()
    name = fields.Method('get_name', dump_only=True)

    @staticmethod
    def get_name(obj):
        locale = Utility.get_current_language()
        try:
            return getattr(obj, 'name_' + locale)
        except AttributeError:
            return obj.name_en


class MultiDealerSchema(Schema):
    dealer_id = fields.Integer(allow_none=True)
