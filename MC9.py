from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/producto/<int:producto_id>', methods=['GET'])
def obtener_producto(producto_id):
    mensaje = f"Producto {producto_id} consultado correctamente"
    return jsonify({"mensaje": mensaje})

if __name__ == '__main__':
    app.run(debug=True)
