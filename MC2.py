""" Cliente Simple de Chat: Desarrolla un cliente que se conecte a un servidor de sockets y permita al 
usuario enviar un mensaje simple a través de la terminal. Una vez enviado, el cliente debería cerrar la conexión. """

import socket

#Definimos direccion y puerto 

HOST = '127.0.0.1' # local host
PORT = 65432 #puerto que se va usar


def main():
    #creamos el socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM )

    try:
        client.connect((HOST,PORT)) # se conecta al servidor

        #Se solicita al usuario que ingrese un mensaje 
        mensaje = input("Introdusca un mensaje: ")

        # Se envisa el mensaje al servidor

        client.sendall(mensaje.encode('utf-8'))

    finally:
        #cerrar la conexion 
        client.close()
        print("conexion cerrada")

if __name__ == "__main__":
    main()


