from web3 import Web3
import json



#the url of the node that is interacting with the block-chain
infura_url = "HTTP://127.0.0.1:7545"

#connecting our api to the node
web3 = Web3(Web3.HTTPProvider(infura_url))

#checking if the node is connected
web3.isConnected()

#getting the current black number of the whole block chain
web3.eth.blockNumber


# getting balance of a wallet -> its in Wei
balance = web3.eth.getBalance("0x3EBF6416F0A91416c085457dB36214DDcB51a09d")


#converting Wei to ether
web3.fromWei(balance, "ether")

#abi is a json array that describes the smart contract
abi = ""

# address of the smart contract
address =""



### Sending Crypto from one network to another


account_1 = ""

account_2 = ""

private_key = ""

nonce = web3.eth.getTransactionCount (account_1)
tx = {  'nonce': nonce,
        'to': account_2,
        'value': web3. toWei(1, 'ether"),
        'gas': 2000000, gasPrice': web3.toWei('50', 'gwei")
        }
signed_tx = web3.eth.account. signTransaction(tx, private_key)
tx_hash = web3. eth. sendRawTransaction(signed_tx.rawTransaction)
print (tx_hash)