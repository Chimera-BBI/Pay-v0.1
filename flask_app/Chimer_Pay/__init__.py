from flask import Flask
import os

from datetime import timedelta



app                                     = Flask(__name__)

SECRET_KEY                              = os.urandom(32)
app.config['SECRET_KEY']                = SECRET_KEY



from Chimer_Pay import routes