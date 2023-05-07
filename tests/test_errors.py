import pytest


@pytest.mark.parametrize("api_method", [
    "transcription", "summary"
])
@pytest.mark.vcr()
def test_no_transcription(test_client, api_method):
    video_id = "pJ9ffd8C1JU"
    query_string = {'video_url': f'https://www.youtube.com/watch?v={video_id}'}
    response = test_client.post(f'/{api_method}', query_string=query_string)
    assert response.status_code == 200
    assert "Subtitles are disabled for this video" in response.text


@pytest.mark.parametrize("api_method", [
    "transcription", "summary"
])
@pytest.mark.parametrize("video_url", [
    "INCORRECT_URL", None
])
@pytest.mark.vcr()
def test_incorrect_url(test_client, api_method, video_url):
    query_string = {'video_url': video_url}
    response = test_client.post(f'/{api_method}', query_string=query_string)
    assert response.status_code == 200
    assert "Error parsing video URL (if you think video URL is correct, please send me a message, thanks)" in response.text
