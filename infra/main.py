from cla import cla
from ctf import ctf
from vote import vote


class main:
    def simulate_all():
        populated_database = cla.populate_database(
            "/Users/usaidbinshafqat/Documents/Winter/Cryptography/final/infra/Voter_Database.json", 100000)
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
