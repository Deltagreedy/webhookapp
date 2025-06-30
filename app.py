import json

from flask import Flask
from flask import request

import threading



app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p> Hello </p>"

@app.route('/privacypolicy')
def privacy_policy():
    with open('./PrivacyPolicy.html', 'rb') as file:
        privacypolicyhtml = file.read()
    return privacypolicyhtml

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        try:
            print(json.dumps(requests.get_json(), index = 4))
        except:
            pass
        return '<p> This is POST Request! </p>'
    if request.method == 'GET':
        hub_mode = request.args.get('hub.mode')
        hub_challenge = request.args.get('hub.challenge')
        hub_verify_token = request.args.get('hub.verify_token')
        if hub_challenge:
            return hub_challenge
        else:
            return '<p> This is GET Request! </p>'