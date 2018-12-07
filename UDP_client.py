
import numpy as np
import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 9000

many_data = 1000     # this is abuot 46 minutes of acquisition with 3 markers
                        # (increase for longer acquisition time)

markers = [None] * many_data

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

count = 0

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("acquired marker data, counter = ", count)
    
    strs = 'ifff'
    
    data_ump = struct.unpack(strs, data)
    
    markers[count] = np.array(data_ump)
    
    count = count + 1
    
# press ctrl + c when acquisition is finished
# then run te_csv.py
