"""Autenticación Básica con JWT: Implementa un proceso simple para generar y validar un token JWT en una aplicación. 
Este token debería contener un ID de usuario y una fecha de expiración, 
y tu aplicación debería rechazar cualquier solicitud que no incluya un token válido."""

import jwt
import datetime

SECRET_KEY = "tu_secreto_super_secreto"

def generar_token(user_id):
    # Crear el payload con el ID de usuario y la fecha de expiración
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    # Generar el token JWT
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def validar_token(token):
    try:
        # Decodificar el token
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return "El token ha expirado."
    except jwt.InvalidTokenError:
        return "Token inválido."

if __name__ == "__main__":
    user_id = 123
    token = generar_token(user_id)
    print(f"Token generado: {token}")

    # Validar el token generado
    resultado = validar_token(token)
    print(f"Resultado de la validación: {resultado}")

    # Prueba con un token inválido
    resultado_invalido = validar_token("token_invalido")
    print(f"Resultado de la validación con token inválido: {resultado_invalido}")
