while True:
    print("Escribe un numero entre 0 y 99999")
    numero = int (input())
    if 0 <= numero <= 99999:
        break
    print("Numero invalido.Intentalo de nuevo")
print (f"El numero tiene {len(str(numero))}cifras.")