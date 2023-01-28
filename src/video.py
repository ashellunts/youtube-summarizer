from youtube_transcript_api import YouTubeTranscriptApi, Transcript
from youtube_transcript_api.formatters import TextFormatter
from typing import Tuple


def get_transcription(video_id):
    transcript = _get_transcription(video_id)
    return transcript.language_code, TextFormatter().format_transcript(transcript.fetch())


def get_english_transcription(video_id) -> Tuple[str, str]:
    transcript = _get_transcription(video_id)
    transcript_in_english = _translate_to_english(transcript)

    return transcript.language_code, TextFormatter().format_transcript(transcript_in_english.fetch())


# private api


def _translate_to_english(transcript):
    if 'en' in transcript.language_code:
        return transcript

    if not transcript.is_translatable:
        raise Exception("transcript is not translatable")

    return transcript.translate('en')


def _get_transcription(video_id) -> Transcript:
    return YouTubeTranscriptApi.list_transcripts(video_id).find_transcript(['en-US', 'en', 'ru', 'de'])
