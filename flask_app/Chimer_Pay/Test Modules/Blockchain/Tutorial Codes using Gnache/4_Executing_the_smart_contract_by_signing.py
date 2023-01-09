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
print(contract.functions.greet().call())


# Defining the Ethereum addresses of two accounts
account_1 = "0xf2e2a0d733f903A858E1fd13Abd5b13b408B46f8"

# Defining the private key of the first account
private_key = "9f802b1193debbaf4478482d86a5db382a7bbd56bc7a2b7114c398afab75442b"

# Getting the nonce (number of transactions sent) of the first account
nonce = web3.eth.getTransactionCount(account_1)


# Get the transaction hash of the deployment
transaction = contract.functions.setGreeting('Got the concept!').build_transaction(
                                                                                {
                                                                                    "gasPrice": web3.eth.gas_price,
                                                                                    "from" : account_1,
                                                                                    "nonce" : nonce
                                                                                }

                                                                                )


#sign transaction
signed_transaction = web3.eth.account.sign_transaction(transaction, private_key = private_key)

#transction hash
tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)


# # Updating the greeting in the contract
# tx_hash = contract.functions.setGreeting('NEW GREETING!').transact()

# Waiting for the transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)

# Printing the updated greeting in the contract
print('Updated greeting: {}'.format(contract.functions.greet().call()))
