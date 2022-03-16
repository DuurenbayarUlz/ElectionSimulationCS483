from cla import cla
from ctf import ctf
from vote import vote
import os

class main:
    # run the simulation, calling each of the fucntions
    def simulate_all():
        #To find the path of the voter database
        path = os.getcwd() + "\ElectionSimulationCS483-main\Voter_Database.json"
        #To get the number of votes for the similation
        input_number = input("Enter number of voters (max is 100000; use a lower number for faster execution): ")
        # file path of the json, located in the folder as Voter_Database. Replace the filepath.
        # To be replaced with a user input for the filepath.
        
        populated_database = cla.populate_database(
             path, int(input_number))        

        get_decrypted_voter_list = vote.get_decrypt_voter_list(
            populated_database)
        choose_random_vote = vote.choose_random_vote()
        sign_casted_vote = vote.sign_casted_vote()
        verify_casted_vote = vote.verify_casted_vote()
        encrypt_casted_vote_list = vote.aes_encrypt_casted_vote_list(
            verify_casted_vote)
        decrypted_casted_vote_list = ctf.aes_decrypt_casted_vote_list(
            encrypt_casted_vote_list)
        count_votes = ctf.count_votes(decrypted_casted_vote_list)
        winner = ctf.winner(count_votes)

        print("Winner:", winner[1])
        return winner


main.simulate_all()
