#!/bin/bash

function on_exit {
    kill $(ps | grep python | awk '{print $1}')
}

trap on_exit EXIT

export PYTHONDONTWRITEBYTECODE=1
python server.py &
python -m pytest -x -p no:cacheprovider $@ tests
