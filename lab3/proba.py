import random

"""w = (1,2)
total = 3
for i in range(6):
    randomNumber = random.randint(total + 1, total * 2)
    total = total + randomNumber
    w = w + (randomNumber,)
print(w)
print(total)

q = random.randint(total + 1, total * 2)
print(q)

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1

i = 2
while i<q+1:
    if (is_coprime(i,q) == True):
        break;
    i = i+1

print(i)
print(is_coprime(5,1566))

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1



#t = (1,2)
#print(t)
#n = 1
#t = t + (n,)
#print(t)
"""
def byte_to_bits(byte):
    out = []
    for i in range(8):
        out.append(byte & 1)
        byte >>= 1
    return out[::-1]

uzi = "abcdefghij"
n = 4 # chunk length
chunks = [uzi[i:i+n] for i in range(0, len(uzi), n)]
print(chunks)
print(chunks[1])
hossz = len(uzi)
nr = hossz // n
if (hossz % n > 0):
    nr = nr + 1
print(nr)
