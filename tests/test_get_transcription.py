import os
import pytest
from src import video


@pytest.mark.parametrize("video_id, language_code", [
    ("JzPfMbG1vrE", "en"),
    ("JgBvfC8girQ", "ru"),
    ("glaNxVBOdyE", "de"),
])
def test_get_transcription(video_id, language_code, expected_transcription):
    expected_result = language_code, expected_transcription(video_id)
    assert expected_result == video.get_transcription(video_id)


@pytest.fixture()
def expected_transcription(test_dir_path):
    def f(video_id):
        path = os.path.join(test_dir_path, f'{video_id}.txt')
        return open(path).read().strip()
    return f


@pytest.fixture()
def test_dir_path(request):
    return request.fspath.join('..')
