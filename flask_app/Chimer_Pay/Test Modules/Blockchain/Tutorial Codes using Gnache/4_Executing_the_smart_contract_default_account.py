# https://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.7+commit.e28d00a7.js
# online compiler to compile smart contract and push to network


# Importing the Web3 and json libraries
import json
from web3 import Web3

# Defining the URL of the local Ganache node
ganache_url = "http://127.0.0.1:7545"

# Connecting to the Ganache node using the Web3 library
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Setting the default account to the first account in the Ganache node
# web3.eth.defaultAccount = web3.eth.accounts[0]

# Defining the ABI and address of the contract
abi = ""  # Replace with the ABI of your contract

with open("Greeter abi.json","r") as file:
    abi = json.load(file)

address = web3.toChecksumAddress("0xBB59CB1Ec4EBa676C46Dc8575EF8c6618b2674a8")  # Replace with the address of your contract

# Creating a contract object using the Web3 library
contract = web3.eth.contract(address=address, abi=abi)

# Printing the current greeting in the contract
# this is just reading data thus does not require account or any signin
print(contract.functions.greet().call())

# Updating the greeting in the contract
# We are updating the contract memory here thus this requires gas fees !!! 
tx_hash = contract.functions.setGreeting('NEW GREETING!').transact()

# Waiting for the transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)

# Printing the updated greeting in the contract
print('Updated greeting: {}'.format(contract.functions.greet().call()))
