cadena = input("Cadena: ")
invertida = ""

for i in range(len(cadena)-1, -1, -1):
    invertida += cadena[i]

print(invertida)
