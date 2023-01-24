import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


def get_id_from_url(video_url):
    video_id_pattern = r'^(https?\:\/\/)?(youtube\.com|www\.youtube\.com|m\.youtube\.com|youtu\.?be)\/(watch\?v=|embed\/|v\/|.+\?v=)?(?P<id>[-\w]{11})(?:\S+)?$'
    video_id_regex = re.compile(video_id_pattern)

    r = video_id_regex.search(video_url)
    if (r):
        return r.group('id')


def get_transcription(video_id):
    transcript = _get_transcription(video_id)
    return transcript.language_code, TextFormatter().format_transcript(transcript.fetch())


def get_english_transcription(video_id):
    transcript = _get_transcription(video_id)

    language_code = transcript.language_code

    if not 'en' in transcript.language_code:
        if transcript.is_translatable:
            transcript_in_english = transcript.translate('en')
        else:
            raise Exception("no english translation")
    else:
        transcript_in_english = transcript

    return language_code, TextFormatter().format_transcript(transcript_in_english.fetch())


def _get_transcription(video_id):
    return YouTubeTranscriptApi.list_transcripts(video_id).find_transcript(['en-US', 'en', 'ru', 'de'])
