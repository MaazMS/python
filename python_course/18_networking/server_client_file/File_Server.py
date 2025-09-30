# send file to client
import socket

host ='localhost'
port = 60000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
print("server listen the port", port)
s.listen(1)
c, addr = s.accept()
print("connection from", str(addr))

fileName = c.recv(1024)

try:
	f = open("filename", 'rb')
	content = f.read()
	c.send(content)
	f.close()
except FileNotFoundError:
	c.send(b"File Not Found" )

c.close()