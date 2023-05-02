import logging
from src import app
import logging
from logging.handlers import RotatingFileHandler
from flask.logging import default_handler


log_handler_info = RotatingFileHandler('/tmp/myapp.log', maxBytes=1000*1000, backupCount=1)
log_handler_info.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler_info.setFormatter(formatter)

server = app.get_server()
server.logger.setLevel(logging.INFO)
server.logger.addHandler(log_handler_info)

werkzeugLogger = logging.getLogger('werkzeug')
werkzeugLogger.addHandler(log_handler_info)
werkzeugLogger.addHandler(default_handler)

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=8080)
