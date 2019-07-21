#!/usr/bin/python
import socket

HOST = '192.168.0.151'
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# request line
http_data = 'GET /index.php?var1=jmanuel  HTTP/1.1\n'

# header line - all are optional but Host
http_data = http_data + 'Host: 192.168.0.151:8080\n'  # required
http_data = http_data + 'From: irfan.ub@gmail.com\n'
http_data = http_data + 'User-Agent: Lucia Browser\n'
http_data = http_data + 'Keep-Alive: 10\n'
http_data = http_data + 'Accept: text/html\n'
http_data = http_data + 'Connection: close\n'

# separation line - required
http_data = http_data + '\n'    # required

client.send(http_data)

data = client.recv(1024*5)
client.close()
print 'Received\n=================\n', data
