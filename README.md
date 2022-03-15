# CS483 Final Project
## Voting simulation
Contributers: Usaid Shafqat, Hanis Sommerville, and Duurenbayar Ulziiduuren 

What is this? 
A program that simulates an election cycle, where all communication is encrypted using AES and RSA. RSA signs all communications between "voters" and "counters" which are then verified while being sent over AES. Built for CS484: Cryptography final project. 

Instructions to Run: 
- install pycryptodome using pip
- Go to main.py
- In the first function, pass filepath for the included (in current folder) Voter_Database.json (max of 100,000) or Small_Voter_Database.json (max 15), and the number of voters you wish to see in the smiulation as a parameter. 
- Run the main.py file using python main.py or Run functionality from your IDE.
- If you run all 100,000 from Voter_Database.json, the simulation will take about 9 mins. 
 
Results: 
- NOTE: System is rigged to make Pete win by a bigger margin, followed by Teet and then John
- Output should show when voter database is loaded
- Followed by the progress of votes being signed using RSA for each voter
- And then progress of votes being verifying 
- Will show total VALID casted votes (some votes are supposed to be not verifiable on purpose to depict a real life scenario)
- Followed by the Overall Results for each candidate in a hash map 
- And then the final winner

Potential Issues in Running: 
- It might show an error about missing Pycryptodome or Crypto while running, to go about it: 
-> go to directory where python is install (or follow the filepath where the error is)
-> Scroll until you see Crypto or Pycryptodome or similar folders and paste them into the project directory 
-> Replace existing Crypto and Pycryptodome folders
