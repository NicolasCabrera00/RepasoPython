
"""
lista = [expresion (elemento) for elemento in objetoIterable]

"""

def calcular_cuadrado(num):
    return num ** 2

lista_numeros = [1,2,3,4,5,6,7,8,9]
nueva_lista = []

for indice in lista_numeros:
    cuadrado = indice ** 2
    nueva_lista.append(cuadrado)

print("Del ciclo for: ", nueva_lista)

nueva_lista = [calcular_cuadrado(indice) for indice in lista_numeros]

print("Lista comprehesion: ", nueva_lista)