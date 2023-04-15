from flask import Flask

app = Flask('app')


@app.route('/api')
def hello_world():
    return 'hello world'


app.run(host='0.0.0.0', port=8080)
