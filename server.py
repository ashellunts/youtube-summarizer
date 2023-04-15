from flask import Flask, request
from src import summary, video_id

app = Flask('app')


@app.route('/api')
def make_summary():
    return summary.make_gpt_3_5_turbo("Hello my name is Alex and I am a software engineer. I live in Germany.")


@app.route('/api2', methods=['POST'])
def make_summary_2():
    video_url = request.args.get('video_url')
    return video_id.get_from_url(video_url)


app.run(host='0.0.0.0', port=8080)
