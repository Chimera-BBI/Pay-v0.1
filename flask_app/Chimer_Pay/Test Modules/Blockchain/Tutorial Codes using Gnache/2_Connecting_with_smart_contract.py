"""
_summary_
    
infura_url: This variable stores the URL of the Infura node that will be used to interact with the Ethereum blockchain. Infura is a service that allows developers to access Ethereum nodes through an API, so they don't need to run their own node.

web3: This variable is an instance of the Web3 class from the web3 library. It is used to connect to an Ethereum node (in this case, the Infura node specified in infura_url) and perform various operations on the blockchain, such as reading data or sending transactions.

abi: This variable stores the application binary interface (ABI) of the contract. The ABI is a JSON object that specifies the functions and variables of the contract, as well as their types. It is needed in order to interact with the contract using the web3 library.

address: This variable stores the Ethereum address of the contract. It is needed in order to create a contract object using the web3 library.

contract: This variable is an instance of the Contract class from the web3 library. It is created using the abi and address variables, and is used to interact with the contract on the blockchain.

total_supply: This variable stores the total number of tokens in the contract. It is obtained by calling the `total    
    
    
"""



# Importing the Web3 and json libraries
import json
from web3 import Web3

# Defining the URL of the Infura node that will be interacting with the Ethereum blockchain
infura_url = "https://mainnet.infura.io/v3/953247d0c42b419aa3416810d625cc8c"

# Connecting the API to the Infura node using the Web3 library
web3 = Web3(Web3.HTTPProvider(infura_url))

# Defining the ABI and address of the contract
abi = ""
address = "Qxd26114cdGEE289AccF82350c8d8487fedB8A0C07"

# Creating a contract object using the ABI and address
contract = web3.eth.contract(address=address, abi=abi)

# Getting the total supply of tokens in the contract
total_supply = contract.functions.totalSupply().call()

# Converting the total supply from Wei to Ether and printing the result
print(web3.fromWei(total_supply, 'ether'))

# Getting and printing the name of the token
print(contract.functions.name().call())

# Getting and printing the symbol of the token
print(contract.functions.symbol().call())

# Defining the address of a wallet
wallet_address = "0x2551d2357c8da54b7d330917ee769d33f1f5b93"

# Getting the balance of the wallet in the contract
balance = contract.functions.balanceOf(wallet_address).call()

# Converting the balance from Wei to Ether and printing the result
print(web3.fromWei(balance, 'ether'))

