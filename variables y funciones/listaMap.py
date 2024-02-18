
def calcular_cuadrado(num):
 return num ** 2

lista_numeros = [1,2,3,4,5,6,7,8,9]
lista_numeros_nueva = []


"""for elemento in lista_numeros:
    res = calcular_cuadrado(elemento)
    lista_numeros_nueva.append(res)

print(lista_numeros_nueva)"""

map_cuadrados = list(map(calcular_cuadrado, lista_numeros))
print(map_cuadrados)