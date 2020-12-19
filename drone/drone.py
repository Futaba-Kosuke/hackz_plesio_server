#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

import threading 
import socket
import sys
import time
import platform  
import time

host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

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
n = 0
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
        
        # once
        if n == 0:
            result = sock.sendto('takeoff'.encode('utf-8'),tello_address)
            time.sleep(5)
            result = sock.sendto("down 80".encode('utf-8'),tello_address)
            n = 1
        #
 

    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break




