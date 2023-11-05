#!/usr/bin/env bash

export FLASK_ENV=development
export FLASK_APP=manage:app
flask db upgrade

export FLASK_APP=wsgi:app
flask run --host=0.0.0.0 --port=5000

