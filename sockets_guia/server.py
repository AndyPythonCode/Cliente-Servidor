import socket

# IP ADDRESS donde va a estar el servidor ubicado
SERVER = socket.gethostbyname(socket.gethostname())  

# El numero de puerto a escuchar (non-privileged ports are > 1023)
PORT = 6000  

#Crear una instancia de sockets para poder crear mi cliente-servidor usando (IPV4) y (TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind() se utiliza para asociar el socket con una interfaz de red y un número de puerto específicos:
    s.bind((SERVER, PORT))

    # listen habilita a accept
    s.listen()

    # bloquea y espera una conexión entrante. Cuando un cliente se conecta, devuelve un nuevo objeto de socket que representa la conexión y una tupla que contiene la dirección del cliente. 
    conn, addr = s.accept()

    #Una cosa que es imperativo entender es que ahora tenemos un nuevo objeto socket de accept(). Esto es importante ya que es el socket que usará para comunicarse con el cliente. Es distinto del socket de escucha que usa el servidor para aceptar nuevas conexiones:
    with conn:
        print('Connected by', addr)
        while True:
            # Esto lee los datos que envía el cliente
            data = conn.recv(1024)
            if not data:
                break
            #(Devuelve los datos capturados) repite utilizando
            conn.sendall(data)