nombres = ["Nico","Lucas", "Tade"]

for elemento in nombres:
    if(elemento == "Lucas"):
       break
    print(elemento)

for elemento in nombres:
    if(elemento == "Lucas"):
       continue
    print(elemento)