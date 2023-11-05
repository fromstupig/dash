#!/bin/bash
exec gunicorn --config /app/ops/gunicorn.py wsgi:app
