import os
import argparse
import requests
import time

from flask import Flask, request
from flask_cors import CORS
from line_bot.bot import broadcast

import json

app = Flask(__name__)
CORS(app)

parser = argparse.ArgumentParser()
parser.add_argument('-pi', '--raspberry_pi', required=True)
parser.add_argument('-dr', '--drone', required=True)

args = parser.parse_args()
raspi_url = args.raspberry_pi
drone_url = args.drone

@app.route('/test', methods=['GET'])
def test():
	return 'Hello World'

@app.route('/controller', methods=['POST'])
def controller():
    data_json = request.data.decode('utf-8')
    data_dict = json.loads(data_json)

    access_cnt = int(data_dict['access_cnt'])

    raspi_payload_str = f'This_is_the_{str(access_cnt)}_customer.'
    requests.get(os.path.join(raspi_url, 'light_board', raspi_payload_str))

    requests.get(os.path.join(drone_url, 'takeoff'))
    time.sleep(5)
    drone_payload_str = str(access_cnt)
    requests.get(os.path.join(drone_url, 'up', drone_payload_str))
    time.sleep(5)
    requests.get(os.path.join(drone_url, 'land'))

@app.route('/line_bot', methods=['POST'])
def line_bot():
	data = request.data.decode('utf-8')
	data = json.loads(data)
	image_url = data['url']
	broadcast(image_url)
	return '200'

app.run(port=80)
