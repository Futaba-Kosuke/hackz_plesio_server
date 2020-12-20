import os
import argparse
import requests
import time

from flask import Flask, request
from flask_cors import CORS
from line_bot.bot import broadcast
from firebase.firebase import Firebase

import json

app = Flask(__name__)
CORS(app)

firebase = Firebase()

parser = argparse.ArgumentParser()
parser.add_argument('-pi', '--raspberry_pi', required=True)
parser.add_argument('-dr', '--drone', required=True)

args = parser.parse_args()
raspi_url = args.raspberry_pi
drone_url = args.drone

@app.route('/test', methods=['GET'])
def test():
	return 'Hello World'

requests.get(os.path.join(drone_url, 'takeoff'))

@app.route('/controller', methods=['GET'])
def controller():
    # アクセス数の取得
    docs = firebase.db.collection('users').get()
    values = [doc.to_dict() for doc in docs]
    access_cnt = int(values[0]['count']) + 1
    # アクセス数の更新
    firebase.db.collection('users').document('access_count').update({
        'count': access_cnt
    })
    
    raspi_payload_str = f'This_is_the_{str(access_cnt)}_customer.'
    requests.get(os.path.join(raspi_url, 'light_board', raspi_payload_str))

    # if access_cnt < 5:
    #     requests.get(os.path.join(drone_url, 'up', '20'))
    #     time.sleep(5)
    # else:
    #     print('a')

    return '200'

@app.route('/land', methods=['GET'])
def land():
    requests.get(os.path.join(drone_url, 'land'))
    time.sleep(5)
    return '200'

@app.route('/line_bot', methods=['POST'])
def line_bot():
	data = request.data.decode('utf-8')
	data = json.loads(data)
	text = data['text']
	broadcast(text)
	return '200'

app.run(port=80)
