from marshmallow import fields, Schema, post_load

from models.core_provider.locale import Locale


class LocaleSchema(Schema):
    __model__ = Locale

    id = fields.String()
    english_name = fields.String()
    is_default = fields.Boolean()

    @post_load
    def make_object(self, data):
        return self.__model__(**data)


locale_schema = LocaleSchema(many=False)
locales_schema = LocaleSchema(many=True)
