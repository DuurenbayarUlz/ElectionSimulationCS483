import random
from encryption import helper_methods, aes_cbc, rsa
from cla import cla
import random

global_decrypted_list = {}  # Global variable for the decrypted list
global_vote_with_signature = {}  # Global variable for selected vote with signature


class vote:
    def get_decrypt_voter_list(populated_database):
        global global_decrypted_list
        encrypted_list = populated_database
        # decrypted_list = aes_cbc.aes_cbc_decryption(encrypted_list)
        decrypted_hash_map = aes_cbc.aes_cbc_decryption(encrypted_list)
        hash_map_string = helper_methods.hash_map_to_str(decrypted_hash_map)
        hash_map_json = helper_methods.hash_map_to_json(hash_map_string)

        global_decrypted_list = hash_map_json
        return global_decrypted_list

    def choose_random_vote():
        candidates = ["Pete", "Teet", "John"]
        return random.choice(candidates)

    def sign_casted_vote():
        global global_vote_with_signature

        voter_hash_map = global_decrypted_list
        list_with_signed_vote = {}
        # count = 0
        for each_voter in global_decrypted_list:
            casted_vote = vote.choose_random_vote()
            signed_vote = rsa.rsa_sign(
                casted_vote, voter_hash_map[each_voter][0], voter_hash_map[each_voter][1])
            list_with_signed_vote[each_voter] = signed_vote
            global_vote_with_signature = list_with_signed_vote

        return list_with_signed_vote

    def verify_casted_vote():
        global global_decrypted_list
        global global_vote_with_signature
        all_votes = []
        for i in global_vote_with_signature:
            if rsa.rsa_verify("Pete", global_decrypted_list[i][2], global_decrypted_list[i][1], global_vote_with_signature[i]):
                #print("Verified, for Pete")
                all_votes.append("Pete")
            elif rsa.rsa_verify("Teet", global_decrypted_list[i][2], global_decrypted_list[i][1], global_vote_with_signature[i]):
                #print("Verified, for Teet")
                all_votes.append("Teet")
            elif rsa.rsa_verify("John", global_decrypted_list[i][2], global_decrypted_list[i][1], global_vote_with_signature[i]):
                #print("Verified, for John")
                all_votes.append("John")
            else:
                print("Not verifiable")
        # print(all_votes, len(all_votes))
        # print("All votes verified")
        return all_votes

    def aes_encrypt_casted_vote_list(casted_vote_list):
        return aes_cbc.aes_cbc_encryption(str(casted_vote_list))
