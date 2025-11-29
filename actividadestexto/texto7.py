cadena = input("Cadena: ")
viejo = input("Carácter a reemplazar: ")
nuevo = input("Carácter nuevo: ")

resultado = ""

for c in cadena:
    if c == viejo:
        resultado += nuevo
    else:
        resultado += c

print(resultado)
