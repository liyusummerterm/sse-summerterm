from flask import request
from flask_socketio import emit, join_room, leave_room, send
from backend.extension import socketio
from backend.api.schema import weather_schema


@socketio.on('connect')
def on_connection():
    send('hello')


@socketio.on('query')
def on_my_event(data):
    emit('getWeatherData', weather_schema(data['city'], data['date']))
