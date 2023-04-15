import pytest
from src import transcription as t

MAX_DIFFERENCE_IN_PERCENTAGE = 3.5


@pytest.mark.parametrize("video_id, expected_language_code, expected_length", [
    ("JzPfMbG1vrE", "en", 195),
    ("JgBvfC8girQ", "ru", 3730),
    ("glaNxVBOdyE", "de", 5199),
])
def test_get_transcription(video_id, expected_language_code, expected_length):
    language_code, transcription = t.get_transcription(video_id)

    assert expected_language_code == language_code
    assert difference_in_percentage(expected_length, len(transcription)) < MAX_DIFFERENCE_IN_PERCENTAGE


def difference_in_percentage(a, b):
    return abs(a - b) / b * 100
