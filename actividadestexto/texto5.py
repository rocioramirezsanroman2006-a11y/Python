cadena = input("Cadena: ")
car = input("Carácter a buscar: ")

encontrado = False

for c in cadena:
    if c == car:
        encontrado = True

if encontrado:
    print("Está en la cadena")
else:
    print("No está")
