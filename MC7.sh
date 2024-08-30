#!/bin/bash

# Instalar la dependencia 'requests' para Python
pip install requests

# Verificar si la instalación fue exitosa
if [ $? -eq 0 ]; then
    echo "requests' se instaló correctamente."
else
    echo "Error al instalar 'requests'."
    exit 1
fi

# Instalar la dependencia 'flask' para Python
pip install flask

# Verificar si la instalación fue exitosa
if [ $? -eq 0 ]; then
    echo " 'flask' se instaló correctamente."
else
    echo "Error al instalar la dependencia 'flask'."
    exit 1
fi

echo "Todas las dependencias se instalaron correctamente."
