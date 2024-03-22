import json

# String en formato JSON
json_string = '{"nombre": "Juan", "edad": 30, "ciudad": "Buenos Aires"}'

# Verificar que json_string es de tipo str
print(f"El tipo de json_string es: {type(json_string)}")

# Convertir el string JSON a un diccionario
diccionario = json.loads(json_string)

# Verificar que diccionario es de tipo dict
print(f"El tipo de diccionario es: {type(diccionario)}")