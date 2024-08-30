from flask import Flask, request, jsonify

# Crear la aplicación Flask
app = Flask(__name__)

# Una lista vacía para almacenar los logs 
logs = []

# Ruta para recibir los logs (POST)
@app.route('/logs', methods=['POST'])
def recibir_log():
    # Obtener los datos del log enviados en la solicitud
    nuevo_log = request.json
    
    # Agregar el log a la lista en memoria
    logs.append(nuevo_log)
    
    # Responder con un mensaje de éxito
    return jsonify({"mensaje": "Log recibido exitosamente"})

# Ruta para ver todos los logs almacenados (GET)
@app.route('/historial', methods=['GET'])
def obtener_logs():
    return jsonify(logs)

# Ruta raíz opcional para evitar el 404 (GET)
@app.route('/', methods=['GET'])
def home():
    return "Bienvenido a tus logs"

# Iniciar el servidor 
if __name__ == '__main__':
    app.run(debug=True)
