import os
from pprint import pprint

import yaml
from flasgger import Swagger

from os import path


def init_app(app, spec):
    data = yaml.load(spec.to_yaml())
    writePath = path.join(path.abspath(path.dirname(__file__)), 'index.yaml')
    with open(writePath, 'w') as file:
        yaml.dump(data, file)
    with app.app_context():
        Swagger(app, template_file=path.join(path.abspath(path.dirname(__file__)), 'index.yaml'))
