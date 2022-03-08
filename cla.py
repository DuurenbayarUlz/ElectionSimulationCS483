class cla: 

    def populate_database(number_of_voters):

        voter_database_CLA = {} 
        for i in range(number_of_voters): 
            voter_database_CLA[i] = create_keys()

        encrypt_voter_database = aes_cbc.aes_cbc_encryption(str(voter_database_CLA))
        
        return encrypt_voter_database 

        # {0: [123, 123, 34545, 456745]}
        # private key object 

        # once converted into bytes, the object is lost
        # cannot decrypt it 

cla_class = cla.populate_database(6)

print(cla_class)