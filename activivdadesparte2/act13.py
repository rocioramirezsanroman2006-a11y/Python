altura = int(input("Altura: "))

for i in range(1, altura + 1):
    cadena = ""
    for j in range(1, i + 1):
        cadena += str(j)
    print(cadena)
