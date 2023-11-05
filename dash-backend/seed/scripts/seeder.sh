#!/usr/bin/env bash

source venv/bin/activate

export FLASK_ENV=development

export FLASK_APP=manage:app
flask db upgrade

export FLASK_APP=cli:app

source seed/scripts/1_init.sh

deactivate
