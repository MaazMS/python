#### socket programming
we're going to establish the communication between the server and the client using the DCP IP protocol while doing socket programming.   

#### Create a server  
step 1 : import socket  
step 2 : host ='localhost'     `name of host`     
step 3 : port = `40000  name of port`    
step 4 : s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
`AF_INET` :  we can specify which version of IP we are going to use.  
This means we are using internet protocol version four AF_INET.     
second parameter is the type of connection whether it's TCP IP or UDP etc..    
`SOCK_STREAM` meanse use TCP IP.  
step 5 :  s.bind((host,port))  
bind method accepts need to pass in a host comma ports dot Listen.   
step 6 : listen(1)  
A listening socket does just what it sounds like. It listens for connections from clients.   
step 7 : accept()  
accept returns two things it returns the connection. It also returns the address from which the request came from or the client's address.    
step 8 : send message by binary form eg `c.send(b""hello covert into binary)` or `c.send("bye".encode())`   
step 9 : close() close the socket.  

#### Create a clinet  

step 1 : import socket   
step 2 : host ='localhost'     `name of host`     
step 3 : port = `40000  name of port`     
step 4 : s.connect((host,port))     
step 5 : receive byte eg `msg = s.recv(1024) # number of byte receive`   
step 6 : decode meaage  eg `msg.decode()` 
step 7 : msg = s.recv(1024)   
step 8 : close() close the clinet.    

#### Email communication  
SMTP library allows us to send out emails.   
to build our email message including the body the subject from to etc. all that will be contained MIMEText  
first body 
second message 

