import socket
import time 


HOST =  '127.0.0.1'
PORT = 65432


import socket
import time

HOST = '127.0.0.1'
PORT = 65432

def start_client():
    # Crear un socket de cliente
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conectar al servidor
        client.connect((HOST, PORT))
        print("Conectado al servidor.")

        # Recibir el mensaje de bienvenida
        welcome_message = client.recv(1024)
        print(f"Mensaje del servidor: {welcome_message.decode('utf-8')}")

        # Enviar datos al servidor
        client.sendall(b'Hola, servidor. Este es un mensaje del cliente.')

        # Esperar un momento para simular una desconexión
        time.sleep(3)  # Espera para permitir al servidor intentar enviar un mensaje

        # Desconectar manualmente
        print("Desconectando manualmente del servidor.")
        client.close()

    except (ConnectionError, socket.error) as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")

if __name__ == '__main__':
    start_client()

