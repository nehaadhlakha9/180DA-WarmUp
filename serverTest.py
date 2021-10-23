import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assigns a port for the server that listens to clients connecting to this port.

host = socket.gethostname()
local_ip = socket.gethostbyname(host) 
print(host) 
print(local_ip)
port = 8080
serv.bind((local_ip, port))
serv.listen(5)
while True:
	conn, addr = serv.accept()
	from_client = ""
	while True:
		data = conn.recv(4096).decode()
		if not data: break
		from_client = data
		print(from_client)
		conn.send("I am SERVER".encode())
	conn.close()
	print("client disconnected")
