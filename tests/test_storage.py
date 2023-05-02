from src import storage
from datetime import datetime


def test_storage():
    storage._delete_calls()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    calls = storage.get_calls()
    assert len(calls) == 0
    storage.add_summary_call(timestamp)
    calls = storage.get_calls()
    assert calls["1"] == timestamp + ",make_summary"
    storage.add_summary_call(timestamp)
    storage.add_summary_call(timestamp)
    calls = storage.get_calls()
    assert calls["1"] == timestamp + ",make_summary"
    assert calls["2"] == timestamp + ",make_summary"
    assert calls["3"] == timestamp + ",make_summary"
    assert len(calls) == 3

    storage.add_transcript_call(timestamp)
    calls = storage.get_calls()
    assert len(calls) == 4
    assert calls["4"] == timestamp + ",get_transcript"
    storage._delete_calls()
    calls = storage.get_calls()
    assert len(calls) == 0
    storage.add_transcript_call(timestamp)
    calls = storage.get_calls()
    assert len(calls) == 1
    assert calls["1"] == timestamp + ",get_transcript"
