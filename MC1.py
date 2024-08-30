""""Configuración Básica de Sockets: Implementa un servidor de sockets básico que escuche en un puerto específico y acepte 
conexiones de un solo cliente. El servidor debería enviar un mensaje de bienvenida al cliente y luego cerrar la conexión."""

import socket


#Definimos direccion y puerto
HOST = '127.0.0.1' #puerto local
PORT =  65432 #puerto que se va usar

#creacion del socket 
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#datos de conexion e inicio del servidor
server.bind((HOST,PORT))
server.listen(1)

print(f"Servidor iniciado{HOST}:{PORT}")

#esperar y aceptar conexion de un cliete

client , address = server.accept()
with client:
    print(f"Conctado por {address}")
    #Eviar mensaje de bienvenida 
    mensaje = "Hola y chau! :)  "
    client.sendall(mensaje.encode('utf-8'))
    #Cerrar la conexion
    print("Conexion Cerrada")

#Cerrar el servidor 
server.close()
print("Servidor cerrado")

