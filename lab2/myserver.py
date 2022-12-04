import socket
from _thread import*
from .mykeys import init_config

def threadfunc(conn1, conn2) :
    while True :
        data = conn1.recv(2048)

        if data :
            conn2.send(data)

init_config()

host="127.0.0.1"
port = 6666
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((host,port))
serverSocket.settimeout(40)
serverSocket.listen(1)

conn1, addr = serverSocket.accept()
conn2, addr = serverSocket.accept()

start_new_thread(threadfunc, ( conn1, conn2 ))
start_new_thread(threadfunc, ( conn2, conn1 ))

while True :
    a = 1
