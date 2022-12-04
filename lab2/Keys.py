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