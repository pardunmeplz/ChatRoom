import json

myChat = []

def getChat(msg= None):
    if msg: myChat.append(msg)
    return json.dumps(myChat)