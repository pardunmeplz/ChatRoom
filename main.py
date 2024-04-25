from flask import Flask, render_template, request
from flask_socketio import emit, SocketIO
import json

myApp = Flask(__name__)
myChat = ['heyyya', 'chiiiiiiiis','wasssuuuup']
socket = SocketIO(app=myApp)

@myApp.route('/')
def Home():
    return render_template("index.jinja", chatData = myChat)

@socket.on("connect")
def connect():
    emit("connect",json.dumps(myChat))

@socket.on("data")
def handleData(data):
    myChat.append(data)
    emit("data",json.dumps(myChat),broadcast=True)

@socket.on("disconnect")
def disconnected():
    print("user disconnected")
    emit("disconnect",f"user {request.sid} disconnected",broadcast=True)

@myApp.route('/add',methods=["POST"])
def Chat():
    data = request.data
    myChat.append(data.decode('UTF-8'))
    print(myChat)
    return 'success', 200

if __name__ == "__main__":
    socket.run(app =myApp, debug=True, port=5000)