import os
import openai
import pytest
from dotenv import load_dotenv
from src import summary


def test_make_summary(check_openai_tests):
    s = summary.make("Hello my name is Alex and I am software engineer. I make apps and sites.")
    assert "software engineer" in s and len(s) > 100


@pytest.fixture(autouse=True)
def init_openapi():
    load_dotenv()
    openai.api_key = os.getenv("OPENAPI_KEY")


def test_make_summary_gpt_3_5_turbo(check_openai_tests):
    s = summary.make_gpt_3_5_turbo("Hello my name is Alex and I am a software engineer. I live in Germany.")
    assert "software" in s and "Germany" in s
