import logging
from src import app
import logging
from flask.logging import default_handler
from logtail import LogtailHandler
import logging
import os

LOGTRAIL_TOKEN = os.environ.get("LOGTRAIL_TOKEN", "dummy")
logtailHandler = LogtailHandler(source_token=LOGTRAIL_TOKEN)


server = app.get_server()
server.logger.setLevel(logging.INFO)
server.logger.addHandler(logtailHandler)

werkzeugLogger = logging.getLogger('werkzeug')
werkzeugLogger.setLevel(logging.INFO)
werkzeugLogger.addHandler(default_handler)
werkzeugLogger.addHandler(logtailHandler)

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=8080)
