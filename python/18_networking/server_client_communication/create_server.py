import socket

host ='localhost'
port = 40000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
print("server listen the port", port)
s.listen(1)
c, addr = s.accept()
print("connection from", str(addr))

# c.send(b""hello covert into binary)
c.send("bye".encode())
c.close()