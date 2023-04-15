from src import app
from pytest import fixture


@fixture
def test_client():
    with app.get_server().test_client() as test_client:
        yield test_client


text = "The video discusses the sexualization of Brooke Shields as a child model and how it perpetuates toxic cultural norms. Gatekeeping is used to control girls and make them desirable to men. Brooke found her own voice but struggled with agency. The video emphasizes the need for better representation and positive role models."


class MockSummarizer:
    def __init__(self, text):
        self.text = text

    def make(self, text):
        return self.text


def test_make_summary_api_1(test_client):
    app.set_mock_summarizer(MockSummarizer(text))
    query_string = {'video_url': 'https://www.youtube.com/watch?v=x7KedT6uvus'}
    response = test_client.post('/api', query_string=query_string)
    assert response.status_code == 200
    assert 'shields' in response.text.lower()


def test_make_summary_api_video_that_needs_2_api_calls(test_client, check_openai_tests):
    query_string = {'video_url': 'https://www.youtube.com/watch?v=FrMRyXtiJkc'}
    response = test_client.post('/api', query_string=query_string)
    assert response.status_code == 200
    assert "vim" in response.text.lower()


def test_make_summary_api_video_that_needs_tldr(check_openai_tests, test_client):
    query_string = {'video_url': 'https://www.youtube.com/watch?v=STpbPXW9-pA'}
    response = test_client.post('/api', query_string=query_string)
    assert response.status_code == 200
    assert "mcconnell" in response.text.lower()
    assert "tldr" in response.text.lower()
    assert "longer version" in response.text.lower()
