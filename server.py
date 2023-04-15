from src import app

server = app.get_server()
server.run(host='0.0.0.0', port=8080)
