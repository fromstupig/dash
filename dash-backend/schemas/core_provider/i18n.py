from flask import g
from marshmallow import Schema, fields, validates, ValidationError, EXCLUDE, post_dump

from schemas.base import IdSchema
from utilities.constant import DEFAULT_LANGUAGE
from utilities.helper import Utility


class I18nSchema(Schema):
    locale_id = fields.String()
    display_text = fields.String()


class I18nProviderSchema(IdSchema):
    class Meta:
        unknown = EXCLUDE

    texts = fields.Nested(I18nSchema, many=True)
    current_text = fields.Method('get_current_display_text', dump_only=True)

    def get_current_display_text(self, obj):
        default = Utility.get_attribute(obj, 'current_text') or ''
        if default:
            return default

        locale_id = Utility.get_attribute(g, 'language', DEFAULT_LANGUAGE)
        locale_id = DEFAULT_LANGUAGE if len(locale_id) > 2 else locale_id
        texts = Utility.get_attribute(obj, 'texts') or []
        for text in texts:
            current_locale_id = Utility.get_attribute(text, 'locale_id')
            display_text = Utility.get_attribute(text, 'display_text')
            rv = display_text if current_locale_id == locale_id else ''

            if rv:
                return rv

            if current_locale_id == DEFAULT_LANGUAGE and display_text:
                default = display_text

            if not default and display_text:
                default = display_text

        return default

    @validates('texts')
    def validate_texts(self, value):
        if len(value) == 0:
            return True

        is_en_text_exist = len(
            [text for text in value if text['locale_id'] == 'en']) == 1

        if not is_en_text_exist:
            raise ValidationError('Must have english text.')

    @post_dump
    def i18n_post_processing(self, data):
        load_all_18n_texts = Utility.get_attribute(g, 'all_language', False)

        if 'all_language' not in g:
            # In case run on entry that doesn't serve http request
            load_all_18n_texts = True

        if not load_all_18n_texts:
            data.pop('texts', None)

        return data
