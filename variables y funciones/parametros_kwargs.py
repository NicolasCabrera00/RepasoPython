def funcion_kwargs(**kwargs):
    for llave, valor in kwargs.items():
        print(f"llave:  {llave} , valor: {valor}")


funcion_kwargs (nombre =  "Nico", apellido = "Cabrera")
