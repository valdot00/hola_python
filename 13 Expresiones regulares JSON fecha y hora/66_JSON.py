#JSON

# convertir datos de un diccionario python a una estructura JSON

producto1 = {"nombre":"silla","color":"blanco","precio":80}

import json

estructura_json = json.dumps(producto1)

print(estructura_json)

print(estructura_json[0])

print(producto1["nombre"])

#convertir una estructura JSON (estructura_json) en un dicionario en python

producto2 = json.loads(estructura_json)

print(producto2)

print(producto2["precio"])