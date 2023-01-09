import os
from Chimer_Pay import app
from .modules import LoginModule
from flask import render_template

from web3 import Web3


"""
Steps Modules and code block


All the steps here are depndent on the connection of wallet and the wallet is the sole point of contact as account 

Module1 : Connect to a wallet to dapp and store public address as session variable
- creating this session vaiable is mandetory for performing transactions
- when performing transaction or any data related query the default page will open promting to connect wallet, page will be blank with a connect wallet option in middle
- things to be done with public address and connection
1. Display user profile data through our server database
2. use read chain to show all transaction performed by the user, basically user logs
3. Provide option to use features




Module 2: Add mobile number to database
1. Wallet should be connected
2. To add mobile number 



Module 3: View Google Contacts

Module 4: Send Stable Coin Using wallet address or phone number or nameing address


Module 5: What if the user data and naming is stored in a private block-chain with only end-point as our server
if to make it double secure, we will validate the sent data with the hash of user phone number and eth address, if this matches we will request to sign transaction

"""




# ------------------- Connect Eth Node -------------------
# using coin base Eth test node 

# import requests


# # Set the URL of the Ethereum node you want to connect to
# infura_url = "https://goerli.ethereum.coinbasecloud.net"
# # Set the API key and username to use for authentication
# api_key = "LFAS4QZUWCIXAUEX56EZ4CFVNU7A7BNP4T4Q3KPQ"
# username = "ROUECLBUF73ULG4A7SZS"

# #Create a session with username and password
# session = requests.Session()
# session.auth = (username, api_key)
 
# #Connect to your Node
# web3 = Web3(Web3.HTTPProvider(infura_url, session=session))

# # Checking if the connection to the node was successful
# if web3.isConnected():
#     print("Successfully connected to the node at", infura_url)
# else:
#     print("Connection to node failed. Please check the URL and try again.")

from flask_jwt_extended import (create_access_token,get_jwt_identity,jwt_required,
                                JWTManager,create_refresh_token,get_jwt_identity,set_access_cookies,
                                set_refresh_cookies,get_jwt,get_csrf_token,unset_jwt_cookies,unset_access_cookies)

from flask import render_template, request, flash, redirect, send_from_directory, url_for,session,request,make_response,jsonify



# login module starts
jwt = JWTManager(app)


def unset_jwt():

    resp = make_response(redirect(url_for('login'),302))
    unset_jwt_cookies(resp)
    return resp

@jwt.unauthorized_loader
def unauthorized_callback(*args,**kwargs):
    # No auth header
    print('unauth token')
    return redirect(url_for('login'),302)

@jwt.invalid_token_loader
def invalid_token_callback(*args,**kwargs):
    # Invalid Fresh/Non-Fresh Access token in auth header
    resp = make_response(redirect(url_for('login'),302))
    print('invalid token')
    unset_jwt_cookies(resp)
    return resp, 302

@jwt.expired_token_loader
def expired_token_callback(*args,**kwargs):
    resp = make_response(redirect(url_for('login'),302))
    print('expired token')
    unset_jwt_cookies(resp)
    return resp,302


@app.after_request
def add_header(r):

    """Adds default header to a page request

    Args:
        r (flask request): request recieved by flask

    Returns:
        flask request: modified request with header
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate",'public, max-age=0'
    r.headers["Pragma"] = "no-cache"    
    r.headers["Expires"] = "0"    
    return r



# @app.route("/get-started")
@app.route("/")
def get_started():
    return render_template("get-started.html")


@app.route("/login")
def login():
    return render_template("enter_phone_number.html")


@app.route("/GetOtp",methods=['GET','POST'])
def GetOtp():

    data = request.form.to_dict()

    status = "Failed"

    try:
        key = LoginModule.start_authentication(data["phoneNumber"])
        status = "Already Exists"
    except:
        LoginModule.sign_up_user(data["phoneNumber"])
        key = LoginModule.start_authentication(data["phoneNumber"])
        status = "New User Created"


    
    session["Authentication Key"] = key

    return (status)
        

@app.route("/VerifyOTP",methods=['GET','POST'])
def VerifyOTP():

    data = request.form.to_dict()

    phone_number    = data["phoneNumber"]
    session_var     = session["Authentication Key"] 
    answer          = data["OTP"]
    results         = LoginModule.verify_otp(phone_number,session_var,answer)

    # raise Exception("Test")

    if "AuthenticationResult" in results:
        access_token    = results["AuthenticationResult"]["AccessToken"]
        resp            = make_response(redirect(url_for('send'),302))
        set_access_cookies(resp,access_token)
        return resp,302
    
    # return "OTP Not Valid"
    flash("OTP Not Valid",'alert')
    return redirect(url_for("login"))



@app.route('/logout')
@jwt_required()
def logout():
    session.clear()
    resp = unset_jwt()
    return resp,302


# # sampel route
# @jwt_required()
# @app.route("/")
# def index():
#     return render_template("index.html")



@app.route("/send")
def send():
    return render_template("send.html")



# @app.route("/getRawTransaction")
# def get_raw_transaction():

#     data = request.form.to_dict()

#     from_address    = data["from"]
#     to_address     = session["to"] 

#         # Defining the ABI and address of the contract
#     abi = ""  # Replace with the ABI of your contract

#     with open("Greeter abi.json","r") as file:
#         abi = json.load(file)

#     address = web3.toChecksumAddress("0xBB59CB1Ec4EBa676C46Dc8575EF8c6618b2674a8")  # Replace with the address of your contract

#     # Creating a contract object using the Web3 library
#     contract = web3.eth.contract(address=address, abi=abi)

#     # Printing the current greeting in the contract
#     print(contract.functions.greet().call())


#     # Defining the Ethereum addresses of two accounts
#     account_1 = "0xf2e2a0d733f903A858E1fd13Abd5b13b408B46f8"

#     # Defining the private key of the first account
#     private_key = "9f802b1193debbaf4478482d86a5db382a7bbd56bc7a2b7114c398afab75442b"

#     # Getting the nonce (number of transactions sent) of the first account
#     nonce = web3.eth.getTransactionCount(account_1)


#     # Get the transaction hash of the deployment
#     transaction = contract.functions.setGreeting('Got the concept!').build_transaction(
#                                                                                     {
#                                                                                         "gasPrice": web3.eth.gas_price,
#                                                                                         "from" : account_1,
#                                                                                         "nonce" : nonce
#                                                                                     }

#                                                                                     )




# # Define a route for transferring tokens
# @app.route("/transfer/<to_address>/<value>")
# def transfer(to_address, value):
