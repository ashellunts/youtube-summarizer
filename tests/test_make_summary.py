import os
import openai
import pytest
from dotenv import load_dotenv
from src import summary


def _test_make_summary():
    s = summary.make("Hello my name is Alex and I am software engineer. I make apps and sites.")
    assert "software engineer" in s and len(s) > 100


@pytest.fixture(autouse=True)
def init_openapi():
    load_dotenv()
    openai.api_key = os.getenv("OPENAPI_KEY")
