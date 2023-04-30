import pytest
from src import summary


@pytest.mark.vcr()
def test_summary_module():
    s = summary.DELETE_make("Hello my name is Alex and I am a software engineer. I live in Germany.")
    assert "software" in s and "Germany" in s
