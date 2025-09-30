# create the file client that will send the name of the file it wants and then display
import socket
s = socket.socket() # set by default
s.connect(("localhost",60000))
filename = input("Enter filename")
s.send(filename.encode())
content = s.recv(1024) # number of byte receive
print(content.decode())
s.close()