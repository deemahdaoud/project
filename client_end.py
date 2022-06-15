# client.py
import time, socket, sys
from datetime import *

print("\nWelcome to Chat app\n")
print("Initialising....\n")


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 8080
print("\nTrying to connect to ", host, "(", port, ")\n")
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat app\nEnter [e] to exit the chat\n")
date_nowh = datetime.now().strftime('(%Y-%m-%d)')
print(date_nowh)
while True:
    date_nowt = datetime.now().strftime('(%H:%M:%S)')
    message = s.recv(1024)
    message = message.decode()
    print(date_nowt,'   ',s_name, ":", message)
    print(date_nowt, end='     ')
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat app!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())

