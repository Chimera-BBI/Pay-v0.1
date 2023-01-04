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
        



# sampel route

# @app.route("/")
# def index():

#     return render_template("index.html")



@app.route("/send")
def send():

    return render_template("send.html")




# # Define a route for transferring tokens
# @app.route("/transfer/<to_address>/<value>")
# def transfer(to_address, value):
