import get_link

def test_get_link():
    video_id = "6AgzfifL4VE"

    url1 = "https://youtube.com/watch?v=6AgzfifL4VE"
    assert get_link.get_link(url1) == video_id

    url2 = "https://m.youtube.com/watch?v=6AgzfifL4VE"
    assert get_link.get_link(url2) == video_id

    url3 = "https://www.youtube.com/watch?v=6AgzfifL4VE"
    assert get_link.get_link(url3) == video_id

    url4 = "https://youtu.be/watch?v=6AgzfifL4VE"
    assert get_link.get_link(url4) == video_id
