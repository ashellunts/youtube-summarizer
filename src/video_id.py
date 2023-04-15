import re


def get_from_url(video_url):
    video_id_pattern = r'^(https?\:\/\/)?(youtube\.com|www\.youtube\.com|m\.youtube\.com|youtu\.?be)\/(watch\?v=|embed\/|v\/|.+\?v=)?(?P<id>[-\w]{11})(?:\S+)?$'
    video_id_regex = re.compile(video_id_pattern)

    r = video_id_regex.search(video_url)
    if (r):
        return r.group('id')
    else:
        return None
