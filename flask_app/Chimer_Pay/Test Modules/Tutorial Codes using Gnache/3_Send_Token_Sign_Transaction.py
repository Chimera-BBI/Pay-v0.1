# Importing the Web3 library
from web3 import Web3

# Defining the URL of the local Ganache node
ganache_url = "http://127.0.0.1:7545"

# Connecting to the Ganache node using the Web3 library
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Defining the Ethereum addresses of two accounts
account_1 = "0x035533aBAD495C581379005262D49b4dF09925A"
account_2 = "0xBBCF4dC04B5d83D33ffec77B25764D25Abb4999"

# Defining the private key of the first account
private_key = "80b3b0e00441d57befb2428df63adffed612dba093fd750844155ad0fe00eb17"

# Getting the nonce (number of transactions sent) of the first account
nonce = web3.eth.getTransactionCount(account_1)

# Defining the transaction dictionary
tx = {
  'nonce': nonce,  # The nonce of the first account
  'to': account_2,  # The recipient of the transaction
  'value': web3.toWei(1, 'ether'),  # The value of the transaction in Wei
  'gas': 2000000,  # The maximum gas limit for the transaction
  'gasPrice': web3.toWei('50', 'gwei')  # The price of gas in Gwei
}

# Signing the transaction using the private key of the first account
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# Sending the signed transaction to the Ethereum network
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# Printing the transaction hash
print(web3. toHex(tx_hash))