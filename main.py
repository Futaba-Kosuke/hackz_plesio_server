import argparse

from flask import Flask, request
from flask_cors import CORS
from line_bot.bot import broadcast

import json

app = Flask(__name__)
CORS(app)

parser = argparse.ArgumentParser()
parser.add_argument('-pi', '--raspberry-pi', required=True)
parser.add_argument('-dr', '--drone', required=True)

args = parser.parse_args()
raspi_url = args.raspberry-pi
drone_url = args.drone

@app.route('/test', methods=['GET'])
def test():
	return 'Hello World'

@app.route('/line_bot', methods=['POST'])
def line_bot():
	data = request.data.decode('utf-8')
	data = json.loads(data)
	image_url = data['url']
	broadcast(image_url)
	return '200'

app.run()
