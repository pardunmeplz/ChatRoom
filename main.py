from flask import Flask, render_template, request
from flask_socketio import emit, SocketIO
import data as d

myApp = Flask(__name__)
socket = SocketIO(app=myApp)

@myApp.route('/')
def Home():
    return render_template("index.jinja")

@socket.on("connect")
def connect():
    msg = {'text': f"user {request.sid} joined!", 'type':'status'}
    emit("message",d.getChat(msg=msg),broadcast=True)

@socket.on("message")
def handleData(msg):
    msg = {'text': msg, 'type':'message'}
    emit("message",d.getChat(msg=msg),broadcast=True)

@socket.on("disconnect")
def disconnected():
    msg = {'text': f"user {request.sid} disconnected :(", 'type':'status'}
    emit("message", d.getChat(msg=msg),broadcast=True)

if __name__ == "__main__":
    socket.run(app =myApp, debug=True, port=5000)