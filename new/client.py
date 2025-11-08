import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    ip = input("Enter the website you want to ping (or 'exit' to quit): ")
    s.send(ip.encode())
    if ip.lower() == 'exit':
        break

    data = s.recv(1024).decode()
    print("Ping Result:", data)

s.close()
