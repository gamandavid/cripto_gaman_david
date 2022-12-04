import socket
from .mykeys import coder, decoder, Blum_Blum_Shub
from _thread import*

print("Minden uzenetet egy uj sorba irt \"stop\" zar.")

host = "127.0.0.1"
port = 6666
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((host,port))

with open("D:\Egyetem\Kripto\Labor\cripto_gaman_david\lab2\config2.txt", "r") as f :
    start = []
    line = f.readline().splitlines()[0]
    myalg = Blum_Blum_Shub
    n = 2
    for i in range(n) :
        start.append(int(f.readline()))


def write() :
    global myalg, start

    while True:
        message = ""
        msg = input()
        while msg!="stop" :
            message += msg + "\r\n" 
            msg = input()
        message = coder(myalg, start, message)
        clientSocket.send(message)


def receive() :
    global start, myalg

    msg = clientSocket.recv(2048)
    if msg :
        print("\n<< ",decoder(myalg, start, msg))


start_new_thread(write, ())
while True:
    receive()
