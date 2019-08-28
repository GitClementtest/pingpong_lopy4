from network import LoRa
import socket
import time
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
while True:
	data=s.recv(64)
	print(data)
	s.send('Ping')
	time.sleep(2)
