from app import create_app
from flask_socketio import SocketIO

socketio = SocketIO()

app = create_app()
socketio.run(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)