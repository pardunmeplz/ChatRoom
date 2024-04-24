from flask import Flask, render_template, request
import json
#from flask_socketio import SocketIO, emit
'''
Routes
/

'''

myApp = Flask(__name__)
myChat = ['heyyya', 'chiiiiiiiis','wasssuuuup']


@myApp.route('/')
def Home():
    return render_template("index.jinja", chatData = myChat)

@myApp.route('/add',methods=["POST"])
def Chat():
    data = request.data
    myChat.append(data.decode('UTF-8'))
    print(myChat)
    return 'success', 200

if __name__ == "__main__":
    myApp.run(debug=True)
