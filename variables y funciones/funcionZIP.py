nombres = ["Nico","Javier","Sofia"]
apellidos = ["Cabrera", "Nasda", "Salcedo"]

nombre_completo = list(zip(nombres,apellidos))
print(nombre_completo)

nombres_unzip, apellidos_unzip = zip(*nombre_completo)
print(nombres_unzip)
print(apellidos_unzip)

for nombres, apellidos in zip(nombres, apellidos):
    print(nombres, apellidos)