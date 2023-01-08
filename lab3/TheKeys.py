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





def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    pass

def create_public_key(private_key):
    """Creates a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    pass


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message

    Hint: think about using `zip` at some point

    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints

    @return list of ints representing encrypted bytes
    """
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

kezd = init_pakli()
print(kezd)
titkos = secreting(solitaire_256, kezd, "alma")
print(titkos)