""" Cuando escribimos un archivo json estamos "serializando", es decir, convertir los datos en bit que puedan ser almacenados o transmitidos 

 """
import json 

persona = {
    "nombre" : "Javier",
    "apellido" : "Quinonez",
    "edad" :  24
}

""" para serializar usamos la funcion  json.dumps()"""

objetoJson = json.dumps(persona, indent=2) ##Le envio como parametro el diccionario, ident es opcional, aca es donde hago la serializacion

with open("persona.json", "w") as archivoJson : ##para crear un archivo nuevo
    archivoJson.write(objetoJson) ##le paso el objeto serializado 


""" Con la libreria json tenemos la posibilidad de usar la funcion json.dump() que nos deja enviar el archivo sin hacer la serializacion """
""" Qeudaria asi """

""" with open("persona.json", "w") as archivoEjemplo :
    json.dump(persona, archivoEjemplo) ##de esta manera no necesitamos usar el paso de la linea 14  """



