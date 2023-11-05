from flask_migrate import Migrate

import services
from factory import create_app
from models.base import db

from models.authorization import *  # noqa
from models.core_provider import *  # noqa
from models.vehicle import *  # noqa
from models.dealer import *  # noqa

app = create_app(__name__, config_name='migration')
flask_migrate = Migrate(app, db, compare_type=True)

services.init_app(app, db)
