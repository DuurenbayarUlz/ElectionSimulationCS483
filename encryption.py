from Crypto.PublicKey import RSA
import json
import ast
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from hashlib import sha512


class rsa:
    def generate_keys_rsa():
        # generate the key pair
        keys = RSA.generate(bits=1024)
        # key_pair d, key_pair n, keypair e
        # https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples
        # extract parts of the keys
        return [keys.d, keys.n, keys.e]

    # create an rsa signature d and n
    def rsa_sign(plaintext, key_pair_d, key_pair_n):
        # turn the plain text into bytes
        data = bytes(plaintext, "utf-8")
        # do something fancy with the data
        hash = int.from_bytes(sha512(data).digest(), byteorder="big")
        # create a signature using the key pairs
        signature = pow(hash, key_pair_d, key_pair_n)
        #print(signature, hex(signature))
        return signature

    # verify the creating signature using e and n
    def rsa_verify(plaintext, key_pair_e, key_pair_n, signature):
        # convert the data to bytes again
        data = bytes(plaintext, "utf-8")
        # do something fancy with the data
        hash = int.from_bytes(sha512(data).digest(), byteorder="big")
        # get the hash from the signature
        hash_from_signature = pow(signature, key_pair_e, key_pair_n)
        # compare with the original signature
        return hash == hash_from_signature

# helper methods to deal with different data types (hash maps most importantly)


class helper_methods:
    # converts hash map to string for encryption
    def hash_map_to_str(hash_map):
        str_hash_map = hash_map.decode("UTF-8")
        return str_hash_map
    # converts hash map to a json for after decryption

    def hash_map_to_json(str_hash_map):
        plain_text_json = ast.literal_eval(str_hash_map)
        return plain_text_json
# AES encryption class


# aes encryption class with encryption and decryption methods
class aes_cbc:
    global key
    # making encryption key used for encryption
    key = get_random_bytes(16)
    # function takes in plain text to encrypt

    def aes_cbc_encryption(plaintext):
        # plain text converted into bytes
        data = bytes(plaintext, "utf-8")
        # cipher is created using a key and AES CBC
        cipher = AES.new(key, AES.MODE_CBC)
        # gets cipher text bytes and adds padding
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        # decode the iv
        iv = b64encode(cipher.iv).decode('utf-8')
        # decoding tehe ciphertext
        ct = b64encode(ct_bytes).decode('utf-8')
        # makes a resulting json with iv and ciphertext that is used later in decryption
        result_json = json.dumps({'iv': iv, 'ciphertext': ct})

        # returns the resulting json
        return result_json

    # decryption function which takes the above mentioned encryption json
    def aes_cbc_decryption(encryption_json):
        try:
            # loads the encryption json
            b64 = json.loads(encryption_json)
            iv = b64decode(b64['iv'])
            ct = b64decode(b64['ciphertext'])
            # gets the cipher using the iv from the json
            cipher = AES.new(key, AES.MODE_CBC, iv)
            # unpads the the cipher for the plaintext
            pt = unpad(cipher.decrypt(ct), AES.block_size)

            return pt
        # if the decryption is worng, it throws an error
        except (ValueError, KeyError):
            print("Incorrect decryption")
