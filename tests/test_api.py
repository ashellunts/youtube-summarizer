import requests


def test_make_summary_api(check_openai_tests):
    response = requests.post(
        "http://localhost:8080/api?video_url=https://www.youtube.com/watch?v=x7KedT6uvus",
    )
    assert "Shields" in response.text
