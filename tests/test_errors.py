import pytest
from src import storage


@pytest.mark.parametrize("api_method", [
    "transcription", "summary"
])
@pytest.mark.vcr()
def test_no_transcription(test_client, api_method):
    storage._delete_calls()

    video_id = "pJ9ffd8C1JU"
    query_string = {'video_url': f'https://www.youtube.com/watch?v={video_id}'}
    response = test_client.post(f'/{api_method}', query_string=query_string)
    assert response.status_code == 200
    assert "Subtitles are disabled for this video" in response.text
