from socket import *
from datetime import *
import threading
import time
Host='127.0.0.1'
port=8080
server=socket(AF_INET,SOCK_STREAM)
server.bind((Host,port))
server.listen()
clients=[]
nicknames=[]
#brodcast
def brodcast(message):
    for client in clients:
        client.send(message)
def handle (client):
    while True:
        try:
            message=client.recv(1024).decode('utf-8')
            print(f"{nicknames[clients.index(client)]} says {message}")
            brodcast(message.encode())
        except:
            
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            print(f"{nickname} left the conversation!!!!!")
            msg=f"{nickname} left the conversation room!!!!!\n"
            brodcast(msg.encode())
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client,address=server.accept()
        print(f"connected with{str(address)}")
        clients.append(client)

        client.send('nick'.encode('utf-8'))
        nickname=client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        

        print(f"name of client is  {nickname}")
        date_nowt2 = datetime.now().strftime('(%H:%M:%S)')
        brodcast(f"  {date_nowt2}  {nickname} join to conversation room @@@ the subscribes{nicknames}\n".encode('utf-8'))
        client.send(f'new subscribe is {nickname}'.encode('utf-8'))
        
        thread=threading.Thread(target=handle,args=(client,))
        thread.start()
print('server  is running---')
receive()
