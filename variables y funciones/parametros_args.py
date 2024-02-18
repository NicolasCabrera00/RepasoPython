def calcular_perimetro(*args):
    perimetro = 0
    for indice in args:
        perimetro += indice
    return perimetro

perimetro = calcular_perimetro(1,2,3,4)
print(perimetro)