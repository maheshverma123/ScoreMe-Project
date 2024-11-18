import sys
import os

# Add the path to your app
sys.path.insert(0, '/home/ec2-user/ScoreMe-Project/app')

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

# WSGI entry point
application = app

