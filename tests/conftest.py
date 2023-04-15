import pytest


@pytest.fixture(scope='module')
def vcr_config():
    return {
        "filter_headers": [('authorization', 'DUMMY')],
    }


def pytest_addoption(parser):
    parser.addoption('--enable-openai-tests', '-O', action='store_true', dest="enable_openai_tests",
                     default=False, help="enable openai tests")


@pytest.fixture
def check_openai_tests(request):
    if not request.config.getoption("enable_openai_tests"):
        pytest.skip('open ai tests disabled')
