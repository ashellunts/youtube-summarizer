from flask import Flask, request, render_template
from . import summary, video_id
from . import transcription

app = Flask('app')


@app.route('/api', methods=['POST'])
def make_summary():
    video_url = request.args.get('video_url')
    id = video_id.get_from_url(video_url)
    _, transcript = transcription.get_english_transcription(id)
    return summary.make(transcript)


@app.route('/api2', methods=['POST'])
def make_summary_2():
    video_url = request.args.get('video_url')
    id = video_id.get_from_url(video_url)
    _, transcript = transcription.get_english_transcription(id)
    result = summary.make2(transcript)
    if isinstance(result, list):
        return render_template('short_summary.html', summary_paragraphs=result)
    else:
        return "notlist"


def get_server():
    return app
