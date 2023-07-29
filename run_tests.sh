#!/bin/bash

export PYTHONDONTWRITEBYTECODE=1
venv/bin/python -m pytest -x -p no:cacheprovider --vcr-record=none $@ tests
