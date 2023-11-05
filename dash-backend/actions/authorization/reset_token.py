import random
import string
from datetime import datetime, timedelta

from models import db
from models.authorization.reset_token import ResetToken
from models.authorization.user import User


class ResetTokenAction:
    def generate_reset_token(self, user):
        reset_token = ResetToken(
            token=self._generate_token(),
            user_id=user.id,
            expire=datetime.utcnow() + timedelta(hours=2)
        )
        db.session.add(reset_token)
        db.session.commit()

        return reset_token

    def check_reset_token(self, email, token):
        return ResetToken.query \
            .filter_by(token=token) \
            .filter(ResetToken.expire > datetime.utcnow()) \
            .join(User) \
            .filter(User.user_email == email) \
            .first()

    def _generate_token(self, size=6):
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

    def expired(self, reset_token):
        reset_token.expire = datetime.utcnow()
        db.session.commit()


reset_token_action = ResetTokenAction()
