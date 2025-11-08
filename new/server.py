import socket
import os

# Create socket
s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)
print("Server is listening...")

# Accept client connection
c, addr = s.accept()
print("Connected with:", addr)

while True:
    hostname = c.recv(1024).decode()
    if not hostname:
        break
    if hostname.lower() == 'exit':
        print("Client requested to close connection.")
        break

    print(f"Pinging {hostname} ...")

    # Ping the host (works on Windows; use -c for Linux/Mac)
    response = os.system(f"ping -n 1 {hostname} > nul")

    if response == 0:
        c.send(f"{hostname} is reachable ".encode())
    else:
        c.send(f"{hostname} is not reachable ".encode())

c.close()
s.close()
