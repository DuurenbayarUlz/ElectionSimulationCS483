from ast import literal_eval
from encryption import aes_cbc
from vote import main_vote

class ctf: 
    def aes_decrypt_casted_vote_list(encrypted_casted_vote_list):
        return literal_eval(aes_cbc.aes_cbc_decryption(encrypted_casted_vote_list).decode("utf8"))
    
    def count_votes(aes_decrypt_casted_vote_list): 
        vote_result_map = {}
        for i in range(len(aes_decrypt_casted_vote_list)): 
            if aes_decrypt_casted_vote_list[i] in vote_result_map: 
                vote_result_map[aes_decrypt_casted_vote_list[i]] += 1
            
            else: 
                vote_result_map[aes_decrypt_casted_vote_list[i]] = 1
        print(vote_result_map)
        return vote_result_map
    
    def winner(vote_result_map): 
        # return ("Winner", max(vote_result_map, key=vote_result_map.get))
        voter_map_values = sorted(vote_result_map.values())
        voter_map_keys = sorted(vote_result_map, key=vote_result_map.get)
        max_values = max(voter_map_values)
        count_max_values = voter_map_values.count(max_values)

        if count_max_values > 1: 
            return ("Tie", voter_map_keys[-count_max_values::])
        else: return ("Winner", voter_map_keys[-1])

class main_ctf:
    def run(number_of_voters):
        print(ctf.winner(ctf.count_votes(ctf.aes_decrypt_casted_vote_list(main_vote.run_all(number_of_voters)))))

main_ctf.run(6)
