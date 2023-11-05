from actions.base import BaseAction
from models.core_provider.locale import Locale


class LocaleAction(BaseAction):
    def get_all(self, is_active=True):
        query = self.model.query

        if is_active:
            query = query.active()

        return query.all()

    def create(self, id, english_name, is_default):
        locale = Locale(id=id, is_default=is_default, english_name=english_name)

        self.db.session.add(locale)
        self.db.session.commit()
        return locale


locale_action = LocaleAction(model=Locale)
