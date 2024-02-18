import csv

columnas = ["nombre", "apellido", "edad"]
dato = ["Paco", "Botero", 26]

datos_lista = [
    ["Paco", "Botero", 26],
    ["Javier", "Quiñonez", 24],
    ["Emilio", "Tafur", 25]
]
datos_dict = [
    {"nombre": "Paco", "apellido": "Botero", "edad": 26},
    {"nombre": "Javier", "apellido": "Quiñonez", "edad": 24},
    {"nombre": "Emilio", "apellido": "Tafur", "edad": 25}
]

##Maneras de escribir en archivos csv

""" archivo = open("Datos.csv", "w")
writer = csv.writer(archivo, delimiter= ",")
archivo.close() """

##Para enviar set de datos

""" with open("Datos.csv", delimiter = "w", newline = "") as archivo: #indica que vamos a trabajar con el archivo abierto, ademas  
                                                                #un alias a dicho archivo con "as" asignamos
    writer = csv.writer(archivo, delimiter=",")
    writer.writerow(columnas)           ##.writerrow() crea una fila con los datos que pasamos como parametros
    writer.writerow(dato) """

##Para enviar una lista anidada, solo cambio writerow por writerows 

""" with open("datos.csv","w", newline="") as archivo:
    writer = csv.writer(archivo, delimiter=",")
    writer.writerow(columnas)
    writer.writerows(datos_lista) """

##Para enviar diccionarios, el lugar de usar writer uso dicwriter

with open("datos.csv", "w", newline="") as archivo:
    writer = csv.DictWriter(archivo, fieldnames= columnas) ##se refiere a la variable de la linea 3
    writer.writeheader()  ##para que nos escriba la primera fila con los nombres de "columnas"
    writer.writerows(datos_dict)    






