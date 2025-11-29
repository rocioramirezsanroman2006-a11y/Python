print("Piensa un número del 1 al 100...")

minimo = 1
maximo = 100
respuesta = ""

while respuesta != "igual":
    intento = (minimo + maximo) // 2
    print("¿Es", intento, "?")
    respuesta = input("Responde: mayor, menor o igual: ")

    if respuesta == "mayor":
        minimo = intento + 1
    elif respuesta == "menor":
        maximo = intento - 1

print("¡Adiviné el número!")
