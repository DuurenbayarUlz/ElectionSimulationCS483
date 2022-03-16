from ast import literal_eval
from encryption import aes_cbc
from ast import literal_eval
import json
import plotext as plt


# ctf class to count votes and find respective winner
class ctf:
    # decrypting the casted vote list
    def aes_decrypt_casted_vote_list(encrypted_casted_vote_list):
        # return the original data type of the encrypted casted vote list
        return literal_eval(aes_cbc.aes_cbc_decryption(encrypted_casted_vote_list).decode("utf8"))

    # couting for each of the candidate
    def count_votes(aes_decrypt_casted_vote_list):
        # initializing empty map to hold candidate name and vote count as key and valyes
        vote_result_map = {'Pete': 0, 'Teet': 0, 'John': 0}
        # iterating through the list to find each candidate and set count as valye
        candidates = ["Teet", "Pete", "John"]
        votes = [vote_result_map.get('Teet'), vote_result_map.get('Pete'), vote_result_map.get('John')]
        plt.bar(candidates, votes, orientation="horizontal", width=0.2)
        plt.title("Vote counts")
        plt.show()
        for i in range(len(aes_decrypt_casted_vote_list)):
            if aes_decrypt_casted_vote_list[i] in vote_result_map:
                vote_result_map[aes_decrypt_casted_vote_list[i]] += 1
            else:
                vote_result_map[aes_decrypt_casted_vote_list[i]] = 1
            candidates = ["Teet", "Pete", "John"]
            votes = [vote_result_map.get('Teet'), vote_result_map.get('Pete'), vote_result_map.get('John')]
            plt.bar(candidates, votes, orientation="horizontal", width=0.2)
            plt.show()
            plt.clear_plot()

        print("Total Verified Casted Votes:", sum(vote_result_map.values()))
        # exporting the result map to a json for the front end
        # with open("/Users/usaidbinshafqat/Documents/Winter/Cryptography/final/front/result.json", "w+") as f:
        #     json.dump(vote_result_map, f)
        return vote_result_map

    # finding the winner from the map with most votes,
    # deals with draws as well, more details in the following code
    def winner(vote_result_map):
        # sorted the values from the vote result map
        voter_map_values = sorted(vote_result_map.values())
        # sorted the keys from the vote result map
        voter_map_keys = sorted(vote_result_map, key=vote_result_map.get)
        # getting the max values from the sorted values to find the winner
        max_values = max(voter_map_values)
        # getting the count of the max values (to deal with the ties).
        # logic: if there's more than one max value, it means there's a tie between some candidates
        count_max_values = voter_map_values.count(max_values)
        # shows overrall results
        print("Overall Results", vote_result_map)
        print("finding winner")
        # some more dealing with the ties: if the count is more than one,
        # then return the last ("count of max values") from the end, as those
        # candiadates will be the ones tied
        if count_max_values > 1:
            return ("Tie", voter_map_keys[-count_max_values::])
        # if there's only one instance of the max value, that would be our winner
        else:
            return ("Winner", voter_map_keys[-1])
