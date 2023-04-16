from flask import Flask, request, render_template
from . import summary, video_id
from . import transcription

app = Flask('app')


@app.route('/summary', methods=['POST'])
def make_summary():
    video_url = request.args.get('video_url')
    id = video_id.get_from_url(video_url)
    _, transcript = transcription.get_english_transcription(id)
    result = summary.make2(transcript)
    if isinstance(result, list):
        return render_template('short_summary.html', summary_paragraphs=result)
    else:
        tldr = result["tldr"]
        longer_summary = result["longer_summary"]
        return render_template('long_summary.html', tldr=tldr, summary_paragraphs=longer_summary)


@app.route('/transcription', methods=['POST'])
def make_transcription():
    video_url = request.args.get('video_url')
    id = video_id.get_from_url(video_url)
    _, transcript = transcription.get_transcription(id)
    return render_template('transcription.html', transcript=transcript)


def get_server():
    return app
