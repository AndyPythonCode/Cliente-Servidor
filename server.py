import socket
import threading

#Configuraciones basicas
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 8080
FORMAT = 'utf-8'
AMOUNT_OF_BYTES = 1024
DISCONNECT = ('exit','exit()')
SERVER_MESSAGES = ('Mensaje recibido','Disconnect')

#Creando 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER,PORT))

#Envio y entrega de mensajes...
def client_mananger(client, client_addr):
    print(f"Client: {client_addr}")
    try:
        connected = True
        while connected:
            #Recibiendo mensaje del usuario
            data = client.recv(AMOUNT_OF_BYTES).decode(FORMAT)
            if data:
                print(f"User {client_addr}: {data}")
                if data.lower() in DISCONNECT:
                    client.sendall(SERVER_MESSAGES[1].encode(FORMAT))
                    connected = False
                else:
                    client.sendall(SERVER_MESSAGES[0].encode(FORMAT))
        client.close()
    except ConnectionResetError as e:
        print(f"User leaves: {client_addr}")
        client.close()

#Colocando el servidor a escuchar la diferentes peticiones y crea un hilo a cada una
def start():
    s.listen()
    while True:
        client, client_addr = s.accept()
        thread = threading.Thread(target=client_mananger, args=(client,client_addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print(f"SERVER RUNNING ON {SERVER}:{PORT}")
start()