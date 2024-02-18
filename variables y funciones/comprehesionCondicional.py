"""
lista = [expresion(elemento) for elemento in objetoIterable if condicion]
lista =  [expresion(elemento) for elemento in objetoIterable ]

"""

def calcular_cuadrado(num):
    return num ** 2
def esPar(num):
    return num % 2 == 0

listaNumero = [1,2,3,4,5,6,7,8,9]

listaCuadradoPares = [calcular_cuadrado(indice) for indice in listaNumero if esPar(indice)]
print(listaCuadradoPares)

listaCuadradoPares_2 = [calcular_cuadrado(num) if esPar(num) else 0 for num in listaNumero]
print(listaCuadradoPares_2)
