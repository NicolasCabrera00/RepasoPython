import csv

rutaDelArchivo = "csv_Vacio.csv"
archivoAbierto = open(rutaDelArchivo, "w") ##Open (Ubicacion del archivo en sistema, metodo de escritura)
writer = csv.writer(rutaDelArchivo, ",") ##csv.writer (Ubicacion del archivo en sistema, separador de columnas)
archivoAbierto.close() ##ultimo paso para crear el archivo
