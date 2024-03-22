#!/bin/bash

# Verificar si se proporcionó un archivo como argumento
if [ $# -eq 0 ]; then
    echo "No proporcionó un archivo como argumento"
    exit 1
fi

archivo="$1"

# Verificar si el archivo existe
if [ ! -f "$archivo" ]; then
    echo "El archivo '$archivo' no existe."
    exit 1
fi

#verifica que existe la linea 99
if [ $(wc -l < "$archivo") -lt 99 ]; then
    echo "El archivo '$archivo' no tiene 99 líneas."
    exit 1
fi

# Imprimir la línea 99 del archivo usando sed
sed -n '99p' "$archivo"
