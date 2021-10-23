import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
local_ip = socket.gethostbyname(host)
print(host)
print(local_ip)

port = 8080
client.connect(("192.168.1.67", 8080))
client.send("I am CLIENT".encode())
from_server = client.recv(4096).decode()
client.close()
print(from_server)
