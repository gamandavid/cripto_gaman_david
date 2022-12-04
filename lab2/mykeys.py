from Cryptodome.Util import number
import random

# XOR
def byte_xor(ba1, ba2):
    return bytes([a ^ b for a, b in zip(ba1, ba2)])


# Folyamattikosito
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


# Kodolo
def coder(myalg, start, msg) :
    secret = secreting(myalg, start, msg.encode())
    return b''.join(secret)


# Dekodolo
def decoder(myalg, start, msg) :
    secret = secreting(myalg, start, msg)
    return (b''.join(secret)).decode()  


# Blum-Blum-Shub
def Blum_Blum_Shub(start) :
    n = start[0]
    x0 = start[1]
    z= []
    for i in range(8) :
        x1 = (x0**2) % n
        z.append(str(x1 % 2))
        x0 = x1
    return (int("".join(z), 2), [n, x0])    


# 512 szamjegyu primet general
def gen_prime() :
    p = number.getPrime(512)
    while p % 4 != 3 :
        p = number.getPrime(512)
    return p


def init_n() :
    p = gen_prime()
    q = gen_prime()
    return p*q


def init_x0(n) :
    s = number.getRandomRange(1, n)
    return (s**2) % n    


# Megirja a konfiguracios filet
def init_config() :
    with open("D:\Egyetem\Kripto\Labor\cripto_gaman_david\lab2\config2.txt", "w") as f :
        n = init_n()
        kezd = [n, init_x0(n)]
        f.write('blum-blum-shub\n')
        for i in kezd :
            f.write(str(i) + '\n')
    f.close()    

# init_config()    