
lista_numeros = [1,2,3,4,5,6,7,8,9]

nueva_lista = {num for num in lista_numeros if num % 2 == 0}

print(nueva_lista)

vocales = "aeiou"

diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}

print(diccionario)