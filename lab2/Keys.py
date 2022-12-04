import random

def byte_xor(ba1, ba2):
    return bytes([a ^ b for a, b in zip(ba1, ba2)])

def secreting(myalg, start, msg) :
    (mykey, start) = myalg(start)
    k = mykey.to_bytes(1,"big")

    secret = []
    for letter in msg :
        b = letter.to_bytes(1,"big")
        secret.append(byte_xor(b, k))

        (mykey, start) = myalg(start)
        k = mykey.to_bytes(1,"big")
    return secret

def coder(myalg, start, msg) :
    secret = secreting(myalg, start, msg.encode())
    return b''.join(secret)

def decoder(myalg, start, msg) :
    secret = secreting(myalg, start, msg)
    return (b''.join(secret)).decode()  


def Blum_Blum_Shub(start) :
    n = start[0]
    x0 = start[1]
    z= []
    for i in range(8) :
        x1 = (x0**2) % n
        z.append(str(x1 % 2))
        x0 = x1
    return (int("".join(z), 2), [n, x0])    