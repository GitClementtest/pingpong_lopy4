from network import LoRa
import socket
import time
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
while True:
	if s.recv(64) == b'Ping':
		print('Pong sending')
		s.send('Pong')
	time.sleep(2)
