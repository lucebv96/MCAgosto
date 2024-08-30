import socket

HOST = '127.0.0.1'
PORT = 65432

def start_server():
    # Crear un socket de servidor
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlazar el socket a la dirección y puerto
    server.bind((HOST, PORT))
    # Escuchar conexiones entrantes
    server.listen()

    print(f"Servidor conectado en {HOST}:{PORT}")

    # Manejo de errores
    while True:
        try:
            # Aceptar una conexión entrante
            conn, addr = server.accept()
            with conn:
                print(f"Conectado por {addr}")

                # Intentar enviar un mensaje de bienvenida
                try:
                    # Convertir el mensaje a bytes usando UTF-8
                    welcome_message = 'Conexión establecida.'.encode('utf-8')
                    conn.sendall(welcome_message)
                except (ConnectionResetError, BrokenPipeError) as e:
                    print(f"Error al enviar mensaje: {e}")
                    continue  # Continuar esperando nuevas conexiones

                # Recibir y mostrar datos del cliente
                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print(f"Recibido: {data.decode('utf-8')}")
                    except (ConnectionResetError, BrokenPipeError) as e:
                        print(f"Error al recibir datos: {e}")
                        break

        except (ConnectionError, OSError) as e:
            print(f"Error de conexión o de sistema: {e}")
        except Exception as e:
            print(f"Se ha producido un error inesperado: {e}")

if __name__ == '__main__':
    start_server()
