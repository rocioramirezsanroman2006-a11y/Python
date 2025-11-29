hay_diez = False

nota = int(input("Introduce una nota (0-10) o -1 para terminar: "))

while nota != -1:
    if nota == 10:
        hay_diez = True
    nota = int(input("Introduce otra nota: "))

if hay_diez:
    print("Ha habido al menos un 10")
else:
    print("No hubo ninguna nota 10")
