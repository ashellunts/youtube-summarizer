import os
import openai
import pytest
from dotenv import load_dotenv
from src import summary


@pytest.fixture(autouse=True)
def init_openapi():
    load_dotenv()
    openai.api_key = os.getenv("OPENAPI_KEY")


def test_make_summary_gpt_3_5_turbo(check_openai_tests):
    s = summary.make("Hello my name is Alex and I am a software engineer. I live in Germany.")
    print(s)
    assert "software" in s and "Germany" in s
