from src.mySocket import socket, myApp
import src.myRoutes as routes

if __name__ == "__main__":
    socket.run(app =myApp, debug=True, port=5000)