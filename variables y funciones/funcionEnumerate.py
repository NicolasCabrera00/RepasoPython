"""
enumerate(iterable, start=0)
"""

nombres = ["Nico","Javier","Sofia"]

nombres_enumerados = enumerate(nombres, start=10)

print(list(nombres_enumerados))

for indice, elemento in enumerate(nombres):
    print(indice,elemento)
