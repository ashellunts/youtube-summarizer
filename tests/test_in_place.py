from src import app
import pytest


@pytest.fixture
def test_client():
    with app.get_server().test_client() as test_client:
        yield test_client


@pytest.mark.vcr()
def test_make_summary_api_1(test_client):
    query_string = {'video_url': 'https://www.youtube.com/watch?v=x7KedT6uvus'}
    response = test_client.post('/api', query_string=query_string)
    assert response.status_code == 200
    assert 'shields' in response.text.lower()


@pytest.mark.vcr()
def test_make_summary_api_video_that_needs_2_api_calls(test_client, check_openai_tests):
    query_string = {'video_url': 'https://www.youtube.com/watch?v=FrMRyXtiJkc'}
    response = test_client.post('/api', query_string=query_string)
    assert response.status_code == 200
    assert "vim" in response.text.lower()


@pytest.mark.vcr()
def test_make_summary_api_video_that_needs_tldr(check_openai_tests, test_client):
    query_string = {'video_url': 'https://www.youtube.com/watch?v=STpbPXW9-pA'}
    response = test_client.post('/api', query_string=query_string)
    assert response.status_code == 200
    assert "mcconnell" in response.text.lower()
    assert "tldr" in response.text.lower()
    assert "longer version" in response.text.lower()
