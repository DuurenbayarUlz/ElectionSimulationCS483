import json
class cla: 
    # creates a new data base, taking in the number of voters according to the
    # user's preference. To be changed to a proper input later. 
    def populate_database(): 

        with open('voterDatabse.json') as json_file: 
            ItemData = json.load(json_file)

        print(len(ItemData))
        
        print(type(ItemData))
        
        print(ItemData)

        encrypt_voter_database = aes_cbc.aes_cbc_encryption(str(ItemData))

        return encrypt_voter_database

    # def populate_database():
    #     # creates an empty hash map 
    #     voter_database_CLA = {} 
    #     # hash map is populated with private and public keys as vaules. 
    #     # Keys will be replaced with random usernames later ### 

    #     # encrypts the database hash map under AES CBC using the functions
    #     # hash map is sent in as a string as per the requirement of the function
    #     encrypt_voter_database = aes_cbc.aes_cbc_encryption(str(voter_database_CLA))
        
    #     return encrypt_voter_database 

cla_class = cla.populate_database()
