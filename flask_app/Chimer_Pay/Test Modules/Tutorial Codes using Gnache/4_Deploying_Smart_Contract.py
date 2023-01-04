
#https://youtu.be/umg2fWQX6jM
#https://youtu.be/zCAhMBedPjc


# Import the necessary libraries
import solcx
from solcx import install_solc

import json

install_solc("0.6.0")


from web3 import Web3

# Connect to the Ganache node
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Read the Solidity source code of the contract
with open("Greeter.sol", "r") as file:
    source_code = file.read()

# Compile the contract
compiled_contract = solcx.compile_source(source_code)

# Get the ABI and bytecode of the contract
contract_abi = compiled_contract["<stdin>:Greeter"]["abi"]
contract_bytecode = compiled_contract["<stdin>:Greeter"]["bin"]

with open("Greeter abi.json","w") as file:
    json.dump(contract_abi,file)


# Deploy the contract
contract = web3.eth.contract(
    abi=contract_abi,
    bytecode=contract_bytecode
)

# Defining the Ethereum addresses of two accounts
account_1 = "0xFF3faC0cDf49591f10fC7b1aD60E6E6D0018acF4"
account_2 = "0xBBCF4dC04B5d83D33ffec77B25764D25Abb4999"

# Defining the private key of the first account
private_key = "d75bca71b54dd742e2c0483a092334b8207eea786a40609b84b6a511791e5a95"

# Getting the nonce (number of transactions sent) of the first account
nonce = web3.eth.getTransactionCount(account_1)


# Get the transaction hash of the deployment
transaction = contract.constructor().build_transaction(
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

# Wait for the transaction to be mined
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Get the address of the deployed contract
contract_address = tx_receipt["contractAddress"]

# Create a contract instance using the address of the deployed contract
greeter = web3.eth.contract(
    address=contract_address,
    abi=contract_abi
)
