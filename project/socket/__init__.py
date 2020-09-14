from project import socketio
from flask_socketio import emit


@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')


@socketio.on('message', namespace='/test')
def test_message(message):
    print(f"Recieved: {message}")
    emit('answer', {'data': message['data']})
