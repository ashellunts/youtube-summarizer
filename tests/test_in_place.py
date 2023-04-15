from src import app
from pytest import fixture


@fixture
def test_client():
    with app.get_server().test_client() as test_client:
        yield test_client


def test_in_place(test_client):
    query_string = {'video_url': 'https://www.youtube.com/watch?v=x7KedT6uvus'}
    response = test_client.post('/api', query_string=query_string)
    assert response.status_code == 200
    assert 'shields' in response.text.lower()
