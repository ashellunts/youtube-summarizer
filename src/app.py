import time
import aiohttp
from flask import Flask, request, render_template
from . import summary, video_id
from . import transcription
from . import storage
import youtube_transcript_api
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

    try:
        video_url = request.args.get('video_url')
        id = video_id.get_from_url(video_url)
        _, transcript = transcription.get_transcription(id)
        return render_template('transcription.html', transcript=transcript)
    except youtube_transcript_api._errors.CouldNotRetrieveTranscript as e:
        app.logger.warning(e)
        return "<b style='color:red'>" + e.CAUSE_MESSAGE + "</b>"
    except video_id.ErrorParsingVideoUrl as e:
        app.logger.warning(str(e) + ", url:" + str(video_url))
        return "<b style='color:red'>" + str(e) + "</b>"


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


@app.route('/stats', methods=['GET'])
def info_summary():
    try:
        calls = storage.get_calls()
        stats = {}
        for call in calls.values():
            input_date_format = "%Y-%m-%d"
            date_obj = datetime.strptime(call[:10], input_date_format)
            output_format = "%Y-%m-%d"
            day = date_obj.strftime(output_format)
            if not day in stats:
                stats[day] = {"summary": 0, "transcript": 0}
            if "make_summary" in call:
                stats[day]["summary"] += 1
            else:
                stats[day]["transcript"] += 1
        res = []
        for day in sorted(stats.keys()):
            res.append(f"{day}: summary {stats[day]['summary']}, transcript {stats[day]['transcript']}")
        return render_template('stats.html', stats=res)
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

    try:
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
    except youtube_transcript_api._errors.CouldNotRetrieveTranscript as e:
        app.logger.warning(str(e))
        return "<b style='color:red'>" + e.CAUSE_MESSAGE + "</b>"
    except video_id.ErrorParsingVideoUrl as e:
        app.logger.warning(str(e) + ", url:" + str(video_url))
        return "<b style='color:red'>" + str(e) + "</b>"


def get_server():
    return app
