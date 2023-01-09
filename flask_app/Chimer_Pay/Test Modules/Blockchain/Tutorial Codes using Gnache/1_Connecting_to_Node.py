# Importing the Web3 and json libraries
from web3 import Web3
import json

# Defining the URL of the node that will be interacting with the blockchain
infura_url = "HTTP://127.0.0.1:7545"

# Connecting the API to the node using the Web3 library
web3 = Web3(Web3.HTTPProvider(infura_url))

# Checking if the connection to the node was successful
if web3.isConnected():
    print("Successfully connected to the node at", infura_url)
else:
    print("Connection to node failed. Please check the URL and try again.")

# Getting the current block number of the entire blockchain
current_block_number = web3.eth.blockNumber
print("The current block number is", current_block_number)

# Defining the address of the wallet whose balance we want to check
wallet_address = "0x3EBF6416F0A91416c085457dB36214DDcB51a09d"

# Getting the balance of the wallet in Wei using the getBalance method
balance_in_wei = web3.eth.getBalance(wallet_address)

# Converting the balance from Wei to Ether using the fromWei method
balance_in_ether = web3.fromWei(balance_in_wei, "ether")
print("The balance of the wallet at", wallet_address, "is", balance_in_ether, "Ether")
