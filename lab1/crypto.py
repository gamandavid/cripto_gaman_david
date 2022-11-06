#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: <Gaman David - Mihaly>
SUNet: <gdim2018>

Replace this with a description of the program.
"""
import utils

# Caesar Cipher

def encrypt_caesar(plaintext):
    result = ''
    # Go through the text letter by letter
    for i in range(len(plaintext)):
        letter = plaintext[i]
        # Get the ascii value of the letter
        value = ord(letter)
        # If it's not an upper case letter, dont modify it
        if (value > 64) and (value < 91):
            result += chr((value-ord('A') + 3) % 26 + 65)
        else:
            result +=chr(value)    
    return result    


def decrypt_caesar(ciphertext):
    result = ''
    # Go through the text letter by letter
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        # Get the ascii value of the letter
        value = ord(letter)
        # If it's not an upper case letter, dont modify it
        if (value > 64) and (value < 91):
            result += chr((value-ord('A') - 3) % 26 + 65)
        else:
            result +=chr(value)    
    return result 


# Vigenere Cipher

def encrypt_vigenere(plaintext, keyword):
    result = ''
    # Go through the text and keyword letter by letter
    for i in range(len(plaintext)):
        letter = plaintext[i]
        keyshift = keyword[i]
        # Get the ascii value of the letters
        value = ord(letter) - 65
        keyvalue = ord(keyshift) - 65
        # Shift the text's latter by the key's given value 
        result += chr((value + keyvalue) % 26 + 65) 
    return result 


def decrypt_vigenere(ciphertext, keyword):
    result = ''
    # Go through the text and keyword letter by letter
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        keyshift = keyword[i]
        # Get the ascii value of the letters
        value = ord(letter) - 65
        keyvalue = ord(keyshift) - 65
        # Shift the text's latter by the key's given value 
        result += chr((value - keyvalue) % 26 + 65) 
    return result 


# Merkle-Hellman Knapsack Cryptosystem

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem.

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
    raise NotImplementedError  # Your implementation here

def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    raise NotImplementedError  # Your implementation here


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
    raise NotImplementedError  # Your implementation here

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
    raise NotImplementedError  # Your implementation here


# I . . . . R . . . . Y . . . . Y . . . .
# . A . . . . T . . . . B . . . . H . . .
# . . M . . . . V . . . . A . . . . E . .
# . . . H . . . . E . . . . D . . . . L .
# . . . . U . . . . R . . . . L . . . . P

def encrypt_scytale(plaintext, circumference):
    length = len(plaintext)
    result = ''
    # Iterate through the text by every nth element
    for i in range(circumference):
        for j in range(i,length,circumference):
            result += plaintext[j]       
    return result


def decrypt_scytale(cipheretext, circumference):
    result = ''  
    length = len(cipheretext)
    # If the length is dividable by the circum.
    if length % circumference == 0:
        circumference = circumference - 1
        for i in range(circumference):
            for j in range(i,length,circumference):
                result += cipheretext[j]
    # Else we use another method            
    else:
        i = 0 
        j = 0
        increased = circumference
        result += cipheretext[0]
        while i < length - 1:
            i = i + 1
            if (i % circumference == 0) and (i != 0):
                j = i // circumference
                increased = circumference
            else:
                j = j + increased
                increased = increased - 1
            result += cipheretext[j]    
    return result
    


# W . . . E . . . C . . . R . . . L . . . T . . . E
# . E . R . D . S . O . E . E . F . E . A . O . C .
# . . A . . . I . . . V . . . D . . . E . . . N . .

def encrypt_railfence(plaintext, num_rails):
    result = ''
    return result


def decrypt_railfence(ciphertext, num_rails):
    result = ''    
    return result
