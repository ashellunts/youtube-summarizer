import redis
import os
import json

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
r = redis.Redis.from_url(REDIS_URL, socket_timeout=10)


def add_summary_call(timestamp):
    calls_str = r.get("calls")
    if calls_str == None:
        calls = {}
        calls["1"] = timestamp + ",make_summary"
        r.set("calls", json.dumps(calls))
    else:
        calls = json.loads(calls_str)
        calls[str(len(calls) + 1)] = timestamp + ",make_summary"
        r.set("calls", json.dumps(calls))


def _delete_calls():
    r.delete("calls")


def get_calls():
    calls_str = r.get("calls")
    if calls_str == None:
        return {}
    else:
        return json.loads(calls_str)


def add_transcript_call(timestamp):
    calls_str = r.get("calls")
    if calls_str == None:
        calls = {}
        calls["1"] = timestamp + ",get_transcript"
        r.set("calls", json.dumps(calls))
    else:
        calls = json.loads(calls_str)
        calls[str(len(calls) + 1)] = timestamp + ",get_transcript"
        r.set("calls", json.dumps(calls))
