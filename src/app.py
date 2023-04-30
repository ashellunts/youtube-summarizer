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
    storage.add_transcript_call(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    video_url = request.args.get('video_url')
    id = video_id.get_from_url(video_url)
    _, transcript = transcription.get_transcription(id)
    return render_template('transcription.html', transcript=transcript)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/info', methods=['GET'])
def info():
    calls = storage.get_calls()
    return json.dumps(calls), 200, {'Content-Type': 'application/json'}


@app.route('/summary', methods=['POST'])
async def make_summary():
    storage.add_summary_call(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    start_time = time.time()
    video_url = request.args.get('video_url')
    id = video_id.get_from_url(video_url)
    _, transcript = transcription.get_english_transcription(id)
    result = await summary.make(transcript)
    if isinstance(result, list):
        return render_template('short_summary.html', summary_paragraphs=result)
    else:
        tldr = result["tldr"]
        longer_summary = result["longer_summary"]
        duration_in_second_and_milliseconds = (time.time() - start_time)
        print(f'ALL request took {duration_in_second_and_milliseconds} seconds')
        return render_template('long_summary.html', tldr=tldr, summary_paragraphs=longer_summary)


async def fetch(i, url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(i, " status code", response.status)
            return response.status


def get_server():
    return app
