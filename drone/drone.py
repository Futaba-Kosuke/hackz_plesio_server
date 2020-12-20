#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018
from flask import Flask
from flask_cors import CORS
import threading 
import socket
import sys
import time
import platform  
import time
import cv2
import os
import numpy as np

host = ''
port = 9000
locaddr = (host,port) 

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

#sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

app = Flask(__name__)
CORS(app)

@app.route('/takeoff', methods=['GET'])
def get_takeoff():
    sock.sendto('command'.encode('utf-8'),tello_address)
    result = sock.sendto('takeoff'.encode('utf-8'),tello_address)
    time.sleep(4)
    result = sock.sendto("down 80".encode('utf-8'),tello_address)
    time.sleep(4)


@app.route('/land', methods=['GET'])
def get_land():
    sock.sendto('land'.encode('utf-8'),tello_address)

@app.route('/up/<z>', methods=['GET'])
def get_up(z):
    sock.sendto(f'up {z}'.encode('utf-8'),tello_address)

@app.route('/down/<z>', methods=['GET'])
def get_down(z):
    sock.sendto(f"down {z}".encode('utf-8'),tello_address)

@app.route('/left/<x>', methods=['GET'])
def get_left(x):
    sock.sendto(f'left {x}'.encode('utf-8'),tello_address)

@app.route('/right/<x>', methods=['GET'])
def get_right(x):
    sock.sendto(f'right {x}'.encode('utf-8'),tello_address)

@app.route('/forward/<y>', methods=['GET'])
def get_forward(y):
    sock.sendto(f'forward {y}'.encode('utf-8'),tello_address)

@app.route('/back/<y>', methods=['GET'])
def get_back(y):
    sock.sendto(f'back {y}'.encode('utf-8'),tello_address)

@app.route('/cw/<R>', methods=['GET'])
def get_cw(R):
    sock.sendto(f'cw {R}'.encode('utf-8'),tello_address)

@app.route('/ccw/<R>', methods=['GET'])
def get_ccw(R):
    sock.sendto(f'ccw {R}'.encode('utf-8'),tello_address)


app.run()

while True: 
    try:
        python_version = str(platform.python_version())
        version_init_num = int(python_version.partition('.')[0]) 
       # print (version_init_num)
        if version_init_num == 3:
            msg = input("");
        elif version_init_num == 2:
            msg = raw_input("");
        
        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break
        
        # Send data
        msg = msg.encode(encoding="utf-8")
        result = sock.sendto(msg, tello_address)

    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break





