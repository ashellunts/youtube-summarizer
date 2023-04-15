import pytest
from src import summary


@pytest.mark.vcr()
def test_make_summary_gpt_3_5_turbo(check_openai_tests):
    s = summary.make("Hello my name is Alex and I am a software engineer. I live in Germany.")
    print(s)
    assert "software" in s and "Germany" in s
