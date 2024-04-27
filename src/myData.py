import json

myChat = []
nameMap = {}

def getChat(msg= None):
    if msg: myChat.append(msg)
    return json.dumps(myChat)

def checkToken(token):
    return token in nameMap

def addToken(token, name):
    nameMap[token] = name

def getName(token):
    return nameMap[token]

def removeToken(token):
    del nameMap[token]