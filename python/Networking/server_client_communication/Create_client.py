import socket

s = socket.socket() # set by default
s.connect(("localhost",40000))
msg = s.recv(1024) # number of byte receive

while msg:
	print("recived message to decode", msg.decode())
	msg = s.recv(1024)

s.close()