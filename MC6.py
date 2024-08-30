""" Uso de Argumentos en la CLI: Crea un script simple en Python o Bash que acepte un argumento de 
ubicación desde la línea de comandos e imprima un mensaje de bienvenida personalizado para esa ubicación (ejemplo: "Bienvenido a [Ciudad]"). """

import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: python bienvenida.py [Ciudad]")
        return

    ciudad = sys.argv[1]
    print(f"Bienvenido a {ciudad}")

if __name__ == "__main__":
    main()
