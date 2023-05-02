import time
import aiohttp
from flask import Flask, request, render_template
from . import summary, video_id
from . import transcription
from . import storage
import json
from datetime import datetime
app = Flask('app')


@app.route('/transcription', methods=['POST'])
def make_transcription():
    try:
        storage.add_transcript_call(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as e:
        app.logger.error(e)
        app.logger.error("Failed to add transcript call to stats")

    video_url = request.args.get('video_url')
    id = video_id.get_from_url(video_url)
    _, transcript = transcription.get_transcription(id)
    return render_template('transcription.html', transcript=transcript)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/info', methods=['GET'])
def info():
    try:
        calls = storage.get_calls()
        return json.dumps(calls), 200, {'Content-Type': 'application/json'}
    except Exception as e:
        app.logger.error(e)
        return "internal error", 500


@app.route('/summary', methods=['POST'])
async def make_summary():
    try:
        storage.add_summary_call(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as e:
        app.logger.error(e)
        app.logger.error("Failed to add summary call to stats")

    video_url = request.args.get('video_url')
    id = video_id.get_from_url(video_url)
    _, transcript = transcription.get_english_transcription(id)
    result = await summary.make(app.logger, transcript)
    if isinstance(result, list):
        return render_template('short_summary.html', summary_paragraphs=result)
    else:
        tldr = result["tldr"]
        longer_summary = result["longer_summary"]
        return render_template('long_summary.html', tldr=tldr, summary_paragraphs=longer_summary)


def get_server():
    return app
