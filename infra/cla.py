import json
from encryption import aes_cbc
import itertools


class cla:
    # creates a new data base, taking in the number of voters according to the
    # user's preference. To be changed to a proper input later.
    def populate_database(filepath, input_number):

        with open(filepath) as json_file:
            ItemData = json.load(json_file)

        ItemData = dict(itertools.islice(ItemData.items(), (input_number)))

        encrypt_voter_database = aes_cbc.aes_cbc_encryption(str(ItemData))
        print("Databse Populated")

        return encrypt_voter_database
