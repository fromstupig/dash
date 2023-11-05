from sqlalchemy.ext.hybrid import hybrid_property

from models import db
from models.base import IdMixin


class CoreProviderI18nLink(db.Model):
    __tablename__ = 'core_provider_i18n_links'

    id = db.Column(db.Integer, primary_key=True)

    _texts = db.relationship('CoreProviderI18n', cascade='all,delete', lazy='joined')

    @hybrid_property
    def texts(self):
        return self._texts

    @texts.setter
    def texts(self, value):
        if value is not None:
            self._texts = list(map(lambda item: CoreProviderI18n(**item), value))

    def get_text_by_locale(self, locale_id):
        for text in self.texts:
            if text.locale_id == locale_id:
                return text.display_text

        return None


class CoreProviderI18n(db.Model, IdMixin):
    __tablename__ = 'core_provider_i18n'

    localizable_text_id = db.Column(db.Integer, db.ForeignKey('core_provider_i18n_links.id'), nullable=False)
    display_text = db.Column(db.String(64))

    locale_id = db.Column(db.String(2), db.ForeignKey('locales.id'), nullable=False)
    locale = db.relationship('Locale')
