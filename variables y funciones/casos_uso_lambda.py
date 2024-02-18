lista = [1,2,3,4,5,6,7,8]

numeros_pares = list(filter(lambda num: num%2 == 0, lista))



multiplicarPorDiez = list(map(lambda num : num * 10, lista))

print(multiplicarPorDiez)