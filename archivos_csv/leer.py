import csv

with open("archivos_csv\datos.csv", "r") as archivo:    ##argumento r de read, encoding es opcional
    reader =  csv.reader(archivo)                       ##.reader() para leer el archivo pasado como argumento
    next(reader)                                        ##next es para saltar una fila en el archivo. 
    for fila in reader:                                 ## Utilizo un for para iterar en cada fila
        print(fila)