from Cryptodome.Util import number
import random
import utils

# XOR
def byte_xor(ba1, ba2):
    return bytes([a ^ b for a, b in zip(ba1, ba2)])

def byte_to_bits(byte):
    out = []
    for i in range(8):
        out.append(byte & 1)
        byte >>= 1
    return out[::-1]


# Folyamattikosito
#def secreting(myalg, start, msg) :
#    (mykey, start) = myalg(start)
#    k = mykey.to_bytes(1,"big")

#    secret = []
#    for letter in msg :
#        b = letter.to_bytes(1,"big")
#        secret.append(byte_xor(b, k))

#        (mykey, start) = myalg(start)
#        k = mykey.to_bytes(1,"big")
#     return secret


def solitaire(kezd) :
    return (253, kezd)


# Incializalja a paklit Solitairhez veletlenszeruen
def init_pakli() :
    p = [i for i in range(54)]
    random.shuffle(p)
    return p


# Meghivja az algoritmust es visszateriti a kulcsot
def solitaire_256 ( kezd ) :
    (kulcs1, kezd) = solitaire(kezd)
    (kulcs2, kezd) = solitaire(kezd)
    return ((kulcs1**3 + kulcs2**2)%256, kezd)


# Solitaire
def solitaire( kezd ) :
    pakli = kezd.copy()
    feher = 52
    fekete = 53

   # Feher dzsoker
    feher_ind = pakli.index(feher) #megadja, hogy hol van az 52
    kov = (feher_ind+1)%54
    if kov==0 :
        pakli.remove(feher)
        pakli.insert(kov+1, feher)
    else : 
        pakli[feher_ind], pakli[kov] = pakli[kov], pakli[feher_ind]

    #Fekete kettovel alatta
    fekete_ind = pakli.index(fekete)
    kov = (fekete_ind+2)%54
    pakli.remove(fekete)
    if kov<=1 :
        pakli.insert(kov+1, fekete)
    else :
        pakli.insert(kov, fekete)

    #Csere a dzsokereknel
    ind1 = pakli.index(feher)
    ind2 = pakli.index(fekete)

    if ind1>ind2 :
        ind1, ind2 = ind2, ind1
    
    elso = pakli[0:ind1]
    masodik = pakli[ind1:ind2+1]
    harmadik = pakli[ind2+1: 54]
    pakli = harmadik + masodik + elso

    #Torol also kartyak alapjan
    also = pakli[53]
    if also!=feher and also!=fekete:
        bal = pakli[0 : also+1]
        jobb = pakli[also+1 : 53]
        pakli = jobb + bal + [also]

    felso = pakli[0]
    if felso == feher or felso == fekete :
        return solitaire(pakli)
    
    return (pakli[felso+1], pakli)



# Coprimeot ellenoriz
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1


def generate_private_key(n=8):
    # Superincreasing W
    w = (1,2)
    total = 3
    for i in range(6):
        randomNumber = random.randint(total + 1, total * 2)
        total = total + randomNumber
        w = w + (randomNumber,)

    # Q
    q = random.randint(total + 1, total * 2)

    # R
    r = 2
    while r<q+1:
        if (is_coprime(r,q) == True):
           break;
        r = r+1

    return (w,q,r)


def create_public_key(private_key):
    (w,q,r) = private_key
    # beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q
    b = [i * r % q for i in w]
    return b


def encrypt_mh(message, public_key):
    # Chunkolasa uzenetnek
    n = 8  # Chunk hossza
    chunks = [message[i:i+n] for i in range(0, len(message), n)]
    encrypted = [
        sum(list(map(lambda x,y : x*y,  byte_to_bits(byte), public_key))) 
        for byte in chunks]

    return encrypted


def decrypt_mh(message, private_key):
    (w, q, r) = private_key
    #s = utils.modinv(r, q)

    # c' = cs (mod q)
    c_ = [(c*s) % q for c in message]

    decrypted = ""

    return decrypted


print('hello')    

#kezd = init_pakli()
#print(kezd)
#priv = generate_private_key(8);
#print(priv)
#pub = create_public_key(priv)
#print(pub)

#print(create_public_key(generate_private_key(8)))
#print(encrypt_mh("abcdefghij",pub))