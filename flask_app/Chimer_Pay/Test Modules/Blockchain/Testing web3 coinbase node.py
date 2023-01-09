from web3 import Web3
import json



#the url of the node that is interacting with the block-chain
infura_url = "https://goerli.ethereum.coinbasecloud.net"

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