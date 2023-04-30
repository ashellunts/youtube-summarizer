from src import storage
import json


def _test_redis():
    a = {"foo": "bar", "baz": "qux"}
    storage.set("dict", json.dumps(a))
    a_json = storage.get("dict")
    assert a_json != None
    real = json.loads(a_json)
    assert real == a
