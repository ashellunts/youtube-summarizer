from flask import Flask, request
from . import summary, video_id
from . import transcription

app = Flask('app')
summarizer = summary


def set_mock_summarizer(mock_summarizer):
    global summarizer
    summarizer = mock_summarizer


@app.route('/api', methods=['POST'])
def make_summary_2():
    video_url = request.args.get('video_url')
    id = video_id.get_from_url(video_url)
    _, transcript = transcription.get_english_transcription(id)
    return summarizer.make(transcript)


def get_server():
    return app
