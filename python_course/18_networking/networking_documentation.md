# Python Networking Documentation

## 1. Networking Definition and Characteristics

### What is Networking?

Networking in Python refers to the ability to establish communication between different systems, applications, or processes over a network. It enables data exchange through various protocols and communication methods.

### Key Characteristics

1. **Protocol Support**: Python supports multiple networking protocols (TCP, UDP, HTTP, FTP, SMTP, etc.)
2. **Socket-based Communication**: Uses socket programming for low-level network communication
3. **Cross-platform Compatibility**: Works across different operating systems
4. **Built-in Libraries**: Extensive standard library support for networking operations
5. **Asynchronous Support**: Supports both synchronous and asynchronous networking

### Example - Basic Network Connection Check

```python
import socket

def check_network_connection(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        return True
    except socket.error:
        return False

# Check if Google is reachable
if check_network_connection("google.com", 80):
    print("Network connection is available")
else:
    print("No network connection")
```

## 2. Networking Operations

### Common Networking Operations

1. **Creating Connections**
2. **Sending/Receiving Data**
3. **Handling Multiple Clients**
4. **File Transfers**
5. **Web Requests**

### Example - HTTP GET Request

```python
import urllib.request
import json

def fetch_data(url):
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Fetch JSON data from API
api_url = "https://jsonplaceholder.typicode.com/posts/1"
result = fetch_data(api_url)
if result:
    print(f"Title: {result['title']}")
```

### Example - File Transfer Operation

```python
import socket
import os

def send_file(filename, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        # Send filename first
        s.send(filename.encode())
        
        # Send file data
        with open(filename, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                s.send(data)
    print(f"File {filename} sent successfully")
```

## 3. Networking Methods

### Socket Programming Methods

#### TCP Server Example

```python
import socket
import threading

class TCPServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def handle_client(self, client_socket, address):
        print(f"Connection from {address}")
        try:
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                
                print(f"Received: {data}")
                response = f"Echo: {data}"
                client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()
    
    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        
        try:
            while True:
                client_socket, address = self.socket.accept()
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, address)
                )
                client_thread.daemon = True
                client_thread.start()
        except KeyboardInterrupt:
            print("Server shutting down...")
        finally:
            self.socket.close()

# Usage
if __name__ == "__main__":
    server = TCPServer()
    server.start()
```

#### TCP Client Example

```python
import socket

class TCPClient:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def connect_and_send(self, message):
        try:
            self.socket.connect((self.host, self.port))
            self.socket.send(message.encode('utf-8'))
            
            response = self.socket.recv(1024).decode('utf-8')
            print(f"Server response: {response}")
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.socket.close()

# Usage
client = TCPClient()
client.connect_and_send("Hello, Server!")
```

#### UDP Communication Example

```python
import socket

# UDP Server
def udp_server(host='localhost', port=9999):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")
    
    while True:
        data, client_address = server_socket.recvfrom(1024)
        message = data.decode('utf-8')
        print(f"Received from {client_address}: {message}")
        
        response = f"Echo: {message}"
        server_socket.sendto(response.encode('utf-8'), client_address)

# UDP Client
def udp_client(message, host='localhost', port=9999):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        client_socket.sendto(message.encode('utf-8'), (host, port))
        response, server_address = client_socket.recvfrom(1024)
        print(f"Server response: {response.decode('utf-8')}")
    finally:
        client_socket.close()
```

### HTTP Methods Example

```python
import urllib.request
import urllib.parse
import json

class HTTPClient:
    @staticmethod
    def get_request(url, headers=None):
        try:
            req = urllib.request.Request(url, headers=headers or {})
            with urllib.request.urlopen(req) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            return f"GET Error: {e}"
    
    @staticmethod
    def post_request(url, data, headers=None):
        try:
            if headers is None:
                headers = {'Content-Type': 'application/json'}
            
            json_data = json.dumps(data).encode('utf-8')
            req = urllib.request.Request(url, data=json_data, headers=headers, method='POST')
            
            with urllib.request.urlopen(req) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            return f"POST Error: {e}"

# Usage examples
http_client = HTTPClient()

# GET request
get_result = http_client.get_request("https://httpbin.org/get")
print("GET Result:", get_result)

# POST request
post_data = {"name": "John", "age": 30}
post_result = http_client.post_request("https://httpbin.org/post", post_data)
print("POST Result:", post_result)
```

## Socket Programming Basics

We're going to establish the communication between the server and the client using the TCP IP protocol while doing socket programming.

### Create a Server

**Step 1**: Import socket

```python
import socket
```

**Step 2**: Define host and port

```python
host = 'localhost'  # name of host
port = 40000        # name of port
```

**Step 3**: Create socket object

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- `AF_INET`: Specifies IPv4 protocol
- `SOCK_STREAM`: Specifies TCP connection

**Step 4**: Bind socket to address

```python
s.bind((host, port))
```

**Step 5**: Listen for connections

```python
s.listen(1)  # Listen for 1 connection
```

A listening socket does just what it sounds like. It listens for connections from clients.

**Step 6**: Accept connections

```python
c, addr = s.accept()  # Returns connection and client address
```

Accept returns two things: it returns the connection and the address from which the request came from (client's address).

**Step 7**: Send message in binary form

```python
c.send(b"hello")           # Binary string
c.send("bye".encode())     # Encode string to bytes
```

**Step 8**: Close the socket

```python
s.close()
```  

### Create a Client

**Step 1**: Import socket

```python
import socket
```

**Step 2**: Define host and port

```python
host = 'localhost'  # name of host
port = 40000        # name of port
```

**Step 3**: Create socket and connect

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
```

**Step 4**: Receive data

```python
msg = s.recv(1024)  # Receive up to 1024 bytes
```

**Step 5**: Decode message

```python
decoded_msg = msg.decode()  # Convert bytes to string
```

**Step 6**: Close the client

```python
s.close()
```

## 4. Common Errors in Networking

### 1. Connection Refused Error

**Problem**: Server is not running or port is blocked

```python
import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8080))
except ConnectionRefusedError as e:
    print(f"Connection refused: {e}")
    print("Solution: Check if server is running and port is correct")
except Exception as e:
    print(f"Other error: {e}")
finally:
    s.close()
```

### 2. Timeout Error

**Problem**: Network request takes too long

```python
import socket

def connect_with_timeout(host, port, timeout=5):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((host, port))
        return s
    except socket.timeout:
        print(f"Connection timed out after {timeout} seconds")
        print("Solution: Increase timeout or check network connectivity")
        return None
    except Exception as e:
        print(f"Connection error: {e}")
        return None
```

### 3. Address Already in Use Error

**Problem**: Port is already bound by another process

```python
import socket

def create_server_with_reuse(host, port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Solution: Set socket option to reuse address
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        return server_socket
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print("Address already in use")
            print("Solution: Use SO_REUSEADDR or choose different port")
        return None
```

### 4. DNS Resolution Error

**Problem**: Cannot resolve hostname

```python
import socket

def resolve_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"{hostname} resolved to {ip_address}")
        return ip_address
    except socket.gaierror as e:
        print(f"DNS resolution failed for {hostname}: {e}")
        print("Solution: Check hostname spelling or use IP address directly")
        return None

# Test DNS resolution
resolve_hostname("google.com")
resolve_hostname("invalid-hostname-12345.com")
```

### 5. Broken Pipe Error

**Problem**: Writing to a closed socket

```python
import socket
import signal

def handle_broken_pipe():
    # Ignore SIGPIPE signal to prevent program termination
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 8080))
        
        # Simulate sending data after connection is closed
        for i in range(10):
            try:
                s.send(f"Message {i}".encode())
            except BrokenPipeError:
                print("Broken pipe detected - connection was closed")
                print("Solution: Check connection status before sending data")
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()
```

### 6. Buffer Size Issues

**Problem**: Data truncation due to small buffer size

```python
import socket

def receive_large_data(client_socket):
    """Properly handle large data reception"""
    data = b''
    while True:
        try:
            chunk = client_socket.recv(4096)  # Larger buffer size
            if not chunk:
                break
            data += chunk
            
            # Check if we have received all data (example: look for end marker)
            if b'END' in chunk:
                break
        except socket.error as e:
            print(f"Error receiving data: {e}")
            break
    
    return data.decode('utf-8')
```

### Error Handling Best Practices

```python
import socket
import errno
import time

def robust_socket_operation(host, port, message):
    """Example of robust error handling in socket operations"""
    sock = None
    try:
        # Create socket with timeout
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10.0)
        
        # Connect with retry mechanism
        max_retries = 3
        for attempt in range(max_retries):
            try:
                sock.connect((host, port))
                break
            except (ConnectionRefusedError, socket.timeout) as e:
                if attempt == max_retries - 1:
                    raise
                print(f"Attempt {attempt + 1} failed, retrying...")
                time.sleep(1)
        
        # Send data
        sock.sendall(message.encode('utf-8'))
        
        # Receive response
        response = sock.recv(1024)
        return response.decode('utf-8')
        
    except socket.timeout:
        print("Operation timed out")
    except ConnectionRefusedError:
        print("Connection refused - check if server is running")
    except socket.gaierror:
        print("DNS resolution failed")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if sock:
            sock.close()
    
    return None
```

## Email Communication

### SMTP Example

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """Send email using SMTP"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Add body to email
        msg.attach(MIMEText(body, 'plain'))
        
        # Gmail SMTP configuration
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable security
        server.login(sender_email, sender_password)
        
        # Send email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Error sending email: {e}")

# Usage (use app-specific password for Gmail)
# send_email("your_email@gmail.com", "your_password", "recipient@example.com", 
#           "Test Subject", "This is a test email body.")
```

### Key Points

- **SMTP library**: Allows sending emails
- **MIMEText**: Used to build email message including body, subject, from, to, etc.
- **Body**: First component of the email
- **Message**: Complete email structure
