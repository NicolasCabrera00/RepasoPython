""" Leer un JSON se conoce como deserializar, en python se convierten en diccionarios y los array en listas"""

import json

""" Usamos la funcion load para desearializar """

with open("persona.json", "r") as archivoJson:
    datosJson = json.load(archivoJson)

print(type(datosJson))  ##Primero muestro el tipo de dato
print(datosJson)    ##En segundo lugar, muestro los datos
print(datosJson["nombre"]) ##Asi se muestra solo una fila 