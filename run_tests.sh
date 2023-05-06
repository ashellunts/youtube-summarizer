#!/bin/bash

export PYTHONDONTWRITEBYTECODE=1
python -m pytest -x -p no:cacheprovider --vcr-record=none $@ tests
