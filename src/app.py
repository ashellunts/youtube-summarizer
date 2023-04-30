import time
import aiohttp
import asyncio
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


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/summary2', methods=['POST'])
async def make_summary2():
    start_time = time.time()
    video_url = request.args.get('video_url')
    id = video_id.get_from_url(video_url)
    _, transcript = transcription.get_english_transcription(id)
    result = await summary.make3(transcript)
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


@app.route("/test")
async def test():
    result = ""
    tasks = []
    for i in range(100):
        tasks.append(fetch(i, "https://ashellunts.github.io"))
    responses = await asyncio.gather(*tasks)

    for i, response in enumerate(responses):
        result += str(i) + " status " + str(response) + "<br>"
    return result


def get_server():
    return app
