import json
from encryption import aes_cbc
import itertools


class cla:
    # loads a database from the provided file path, with a certain number ("input_number") of voters
    def populate_database(filepath, input_number):
        # opening the json file from the input filepath
        with open(filepath) as json_file:
            ItemData = json.load(json_file)
        # selecting the provided number of voters from the beginning of the database
        ItemData = dict(itertools.islice(ItemData.items(), (input_number)))
        # encrypting the database using AES encryption to be sent to another function
        encrypt_voter_database = aes_cbc.aes_cbc_encryption(str(ItemData))
        # check to show populated database
        print("Databse Populated")
        # returning the encryped database
        return encrypt_voter_database
