from src import video_id
import pytest


@pytest.mark.parametrize("link", [
    "https://youtube.com/watch?v=6AgzfifL4VE",
    "https://m.youtube.com/watch?v=6AgzfifL4VE",
    "https://www.youtube.com/watch?v=6AgzfifL4VE",
    "https://youtu.be/watch?v=6AgzfifL4VE",
    "https://youtu.be/watch?v=6AgzfifL4VE&t=124",
    "https://youtu.be/6AgzfifL4VE",
])
def test_get_video_id(link):
    assert video_id.get_from_url(link) == "6AgzfifL4VE"
