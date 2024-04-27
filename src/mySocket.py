from flask import Flask, request, session
from flask_socketio import emit, SocketIO
import src.myData as d

myApp = Flask(__name__)
socket = SocketIO(app=myApp)
myApp.secret_key = 'secret'

@socket.on("connect")
def connect():
    msg = {'text': f"user {session['name']} joined!", 'type':'status', 'name':session['name']}
    emit("message",d.getChat(msg=msg),broadcast=True)

@socket.on("message")
def handleData(msg):
    msg = {'text': msg, 'type':'message', 'name':session['name']}
    emit("message",d.getChat(msg=msg),broadcast=True)

@socket.on("disconnect")
def disconnected():
    msg = {'text': f"user {session['name']} disconnected :(", 'type':'status', 'name':session['name']}
    emit("message", d.getChat(msg=msg),broadcast=True)