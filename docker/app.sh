#!/usr/bin/env bash

alembic upgrade head

gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --preload --bind=0.0.0.0:5000
