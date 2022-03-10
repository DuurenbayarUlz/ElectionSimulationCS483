import ast
import binascii
import json
import string
import sys
import time
from base64 import b64decode, b64encode
import gmpy2
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

class rsa: 

    def create_keys(): 
        private_key = rsa.generate_private_key(
            public_exponent=65537, key_size = 2048, backend = default_backend()
        )
        public_key = private_key.public_key()

        # [private key, public key.n, public key.d, public_key]
        return [private_key.d, public_key.public_numbers.n, public_key.public_numbers.d, public_key]
        
    def rsa_encryption(m, publickey): 
        numbers = publickey.public_numbers()
        return gmpy2.powmod(m, numbers.e, numbers.n)

    def rsa_decrypt(m, privatekey): 
        numbers = privatekey.private_numbers()
        return gmpy2.powmod(c, numbers.d, numbers.public_numbers.n)
