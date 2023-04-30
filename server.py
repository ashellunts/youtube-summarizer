from src import app

server = app.get_server()

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=8080)
