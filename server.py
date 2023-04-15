from flask import Flask
from src import summary

app = Flask('app')


@app.route('/api')
def make_summary():
    return summary.make_gpt_3_5_turbo("Hello my name is Alex and I am a software engineer. I live in Germany.")


app.run(host='0.0.0.0', port=8080)
