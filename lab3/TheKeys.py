from Cryptodome.Util import number
import random

# XOR
def byte_xor(ba1, ba2):
    return bytes([a ^ b for a, b in zip(ba1, ba2)])


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

    # 2.
    # Hany chunk van
    hossz = len(message)
    nr = hossz // n
    if (hossz % n > 0):
        nr = nr + 1

    # Vegigmeni chunkokon
    #for i in range()



    return message

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key

    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back

    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r

    @return bytearray or str of decrypted characters
    """
    return message

print('hello')    

#kezd = init_pakli()
#print(kezd)
#priv = generate_private_key(8);
#print(priv)
##pub = create_public_key(priv)
#print(pub)

#print(create_public_key(generate_private_key(8)))