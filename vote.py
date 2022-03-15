import random
from encryption import helper_methods, aes_cbc, rsa
from cla import cla
import random

global_decrypted_list = {}  # Global variable for the decrypted list
global_vote_with_signature = {}  # Global variable for selected vote with signature


# vote class with voting-related methods
class vote:
    # AES decrypting the database and converting to a json
    def get_decrypt_voter_list(populated_database):
        global global_decrypted_list
        encrypted_list = populated_database
        # decrypting function called on the database
        decrypted_hash_map = aes_cbc.aes_cbc_decryption(encrypted_list)
        # turning hash map to string
        hash_map_string = helper_methods.hash_map_to_str(decrypted_hash_map)
        # turning hash map back into json for manipulation
        hash_map_json = helper_methods.hash_map_to_json(hash_map_string)

        global_decrypted_list = hash_map_json
        return global_decrypted_list

    # choosing random vote froma pre popuated BUT RIGGED TO MAKE PETE WIN list of three candidates
    # PETE IS THE LEGEND. PETE FOR THE WIN. PETE ALWAYS.
    def choose_random_vote():
        candidates = ["Pete", "Pete", "Pete", "Pete",
                      "Pete", "Teet" "Teet", "Teet", "John"]
        return random.choice(candidates)

    # signing the votes using RSA encryption so that the voters and their votes are signed
    def sign_casted_vote():
        global global_vote_with_signature
        print("Signing votes")
        # assigning variable to global decrypted lsit
        voter_hash_map = global_decrypted_list
        # list holding the voter and their signature from public and private keys
        list_with_signed_vote = {}
        # itereating through the list to sign the voter
        # using the voter's public and private keys
        count = 0
        for each_voter in global_decrypted_list:
            # random vote chosen
            casted_vote = vote.choose_random_vote()
            # signing the vote using RSA from pubic and private keys in the map for each voter
            signed_vote = rsa.rsa_sign(
                casted_vote, voter_hash_map[each_voter][0], voter_hash_map[each_voter][1])
            # adding the vote for a candidate to the dict to count later
            list_with_signed_vote[each_voter] = signed_vote
            global_vote_with_signature = list_with_signed_vote
            count += 1
            print("RSA Signing Vote #", count)

        return list_with_signed_vote

    # veriffying casted votes
    def verify_casted_vote():
        global global_decrypted_list
        global global_vote_with_signature
        print("Verifying vote")
        # contains all voted candidates names
        all_votes = []
        count = 0
        # iterating thorugh the signed list to verify
        for i in global_vote_with_signature:
            count += 1
            print("RSA Verifying Vote #", count)
            # if the vote is verified for each candidate, it appends to the name of the candiate list to be counted later
            if rsa.rsa_verify("Pete", global_decrypted_list[i][2], global_decrypted_list[i][1], global_vote_with_signature[i]):
                all_votes.append("Pete")
            elif rsa.rsa_verify("Teet", global_decrypted_list[i][2], global_decrypted_list[i][1], global_vote_with_signature[i]):
                all_votes.append("Teet")
            elif rsa.rsa_verify("John", global_decrypted_list[i][2], global_decrypted_list[i][1], global_vote_with_signature[i]):
                all_votes.append("John")
            else:
                # in case the votes are not verifiable (signature is incorrect), return not verifiable and add nothing to the list
                # since it would not be a valid vote
                print("Not verifiable")
        return all_votes

    # Encrypt the list holding candaidate numbers over AES to send to CTF class
    def aes_encrypt_casted_vote_list(casted_vote_list):
        return aes_cbc.aes_cbc_encryption(str(casted_vote_list))
