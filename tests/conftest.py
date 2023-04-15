import pytest
from src import app


@pytest.fixture(scope='module')
def vcr_config():
    return {
        "filter_headers": [('authorization', 'DUMMY')],
        "match_on": ["method", "scheme", "host", "port", "path", "query", "body"],
    }


def pytest_addoption(parser):
    parser.addoption('--enable-openai-tests', '-O', action='store_true', dest="enable_openai_tests",
                     default=False, help="enable openai tests")


@pytest.fixture
def check_openai_tests(request):
    if not request.config.getoption("enable_openai_tests"):
        pytest.skip('open ai tests disabled')


@pytest.fixture
def test_client():
    with app.get_server().test_client() as test_client:
        yield test_client


@pytest.fixture()
def test_dir_path(request):
    return request.fspath.join('..')
