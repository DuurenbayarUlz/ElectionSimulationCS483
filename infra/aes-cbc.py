from Crypto.PublicKey import RSA
import json
import ast
import gmpy2, sys, binascii, string, time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class aes_cbc:
    global key 
    key = get_random_bytes(16)
    def aes_cbc_encryption(plaintext): 
        data = bytes(plaintext, "utf-8")
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        result_json = json.dumps({'iv':iv, 'ciphertext':ct})
        
        return result_json

    def aes_cbc_decryption(encryption_json): 
        try:
            b64 = json.loads(encryption_json)
            iv = b64decode(b64['iv'])
            ct = b64decode(b64['ciphertext'])
            cipher = AES.new(key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            dict_str = pt.decode("UTF-8")
            plain_text_json = ast.literal_eval(dict_str)
            return plain_text_json
        except (ValueError, KeyError):
            print("Incorrect decryption")   

test_hash_map = {1: "one", 2:"two"}
ciphertext_json = aes_cbc.aes_cbc_encryption(str(test_hash_map))

print(aes_cbc.aes_cbc_decryption(ciphertext_json))