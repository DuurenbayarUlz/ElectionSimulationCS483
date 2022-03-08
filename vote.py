import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


class vote:
    def get_decrypt_voter_list(): 
        encrypted_list = cla.populate_database(3)
        decrypted_list = aes_cbc.aes_cbc_decryption(encrypted_list)
        return decrypted_list

    def choose_random_vote(): 
        candidates = ["Pete", "Teet"] 
        return random.choice(candidates)

    # def sign_casted_vote():
        # vote_information = bytes(vote.choose_random_vote(), "utf-8")
        # key = RSA.import_key()
        # return signature

    def verify_casted_vote(): 
        a = 5
        b = 10
        n = vote.get_decrypt_voter_list()[0][1] # public key.n

        # get the public key from the first entry in the hash map, aka the last
        # item in the list stored as value for the hash map
        encrypted_a = rsa.rsa_encryption(a, vote.get_decrypt_voter_list()[0][-1])
        encrypted_b = rsa.rsa_encryption(b, vote.get_decrypt_voter_list()[0][-1])

        encrypted_product = (encrypted_a * encrypted_b) % n

        #### requires the rsa key object here 
        ##### FUCK THS FUCKING PIECE OF SHIT 
        # product = rsa.rsa_decrypt(encrypted_product, expected object)
        product = rsa.rsa_decrypt(encrypted_product, )

        # hypotethically: 
        # product = rsa_decrypt(encrypted_product, private_key)
        # print("{} x {} = {}".format(a,b,product))
    
        # if product == a*b: 
            # print("[PASS]")
        # else: 
            # print("[FAIL]")

# since we're not supposed to technically encrypt using RSA, we don't have to 
# go through the pain of encrypting and decrypting the data, rather just verify
# using pass fail. If pass, we good can proceed but if false then we throw an error

# signatures ^^
        

vote.get_decrypt_voter_list()
vote.choose_random_vote()
# vote.encrypt_casted_vote()