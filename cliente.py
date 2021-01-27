import socket

#Configuraciones basicas
SERVER = '192.168.187.1'
PORT = 8080
FORMAT = 'utf-8'
AMOUNT_OF_BYTES = 1024
WORKING = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))

def send_and_receive():
    global WORKING
    message = input("Write to server: ").encode(FORMAT)
    if message:
        s.sendall(message)
        data = s.recv(AMOUNT_OF_BYTES).decode(FORMAT)
        if data == 'Disconnect':
            WORKING = False
        else:
            print('Received: ', repr(data))

while WORKING:
    send_and_receive()

        
    
