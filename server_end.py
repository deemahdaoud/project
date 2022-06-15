# server.py
import time, socket, sys
from datetime import *

print("\nWelcome to Chat app\n")
print("Initialising....\n")
#time.sleep(1)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 8080
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))

s.listen(5)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat app\nEnter [e] to exit the chat\n")
conn.send(name.encode())
date_nowh = datetime.now().strftime('(%Y-%m-%d)')
print(date_nowh)
while True:
    date_nowt = datetime.now().strftime('(%H:%M:%S)')
    print(date_nowt, end='    ')
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat app!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(date_nowt,'   ',s_name, ":", message)
