import requests


def test_make_summary_api():
    response = requests.get(
        "http://localhost:8080/api?video_url=https://www.youtube.com/watch?v=x7KedT6uvus",
    )
    assert response.text == "hello world"
