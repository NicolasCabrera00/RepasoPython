def calcular_cuadrado (num):
    return num**2


lista_numeros = [1,2,3,4,5,6,7,8,9]

lista_pares = []


for indice in lista_numeros:
    ##cuadrado = calcular_cuadrado(indice) 
    
    
    if(cuadrado := calcular_cuadrado(indice) %2 == 0):
        lista_pares.append(cuadrado)
    else:
        print("El cuadrado de: ", indice)