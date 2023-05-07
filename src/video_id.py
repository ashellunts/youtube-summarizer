import re

ERROR_MESSAGE = "Error parsing video URL (if you think video URL is correct, please send me a message, thanks)"


class ErrorParsingVideoUrl(Exception):
    pass


def get_from_url(video_url):
    if video_url is None:
        raise ErrorParsingVideoUrl(ERROR_MESSAGE)

    video_id_pattern = r'^(https?\:\/\/)?(youtube\.com|www\.youtube\.com|m\.youtube\.com|youtu\.?be)\/(watch\?v=|embed\/|v\/|.+\?v=)?(?P<id>[-\w]{11})(?:\S+)?$'
    video_id_regex = re.compile(video_id_pattern)

    r = video_id_regex.search(video_url)
    if (not r):
        raise ErrorParsingVideoUrl(ERROR_MESSAGE)

    return r.group('id')
