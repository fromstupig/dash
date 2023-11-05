from os import path
from string import Template

from flask_mail import Message, Mail

from utilities.constant import root_dir


class EmailService:
    def __init__(self):
        self._cached_template = {}
        self.sender = Mail()

    def load_body_template(self, name):
        body_template = self._cached_template.get(name, None)
        if body_template is None:
            dir_name = root_dir()
            file_path = path.join(dir_name, 'templates', name)
            try:
                with open(file_path) as fp:
                    body_template = Template(fp.read())
                    self._cached_template[name] = body_template
            except Exception as _:
                raise FileNotFoundError

        return body_template

    def send_forgot_password_email(self, reset_token):
        body_template = self.load_body_template('forgot_password')

        body = body_template.substitute(reset_token=reset_token.token)

        message = Message(
            subject='Reset password',
            recipients=[reset_token.user.email],
            body=body
        )

        self.sender.send(message)


email_service = EmailService()
