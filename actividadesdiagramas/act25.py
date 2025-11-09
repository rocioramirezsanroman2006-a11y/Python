nota = int(input("Escribe tu nota (entera, entre 0 y 10): "))

if nota < 0 or nota > 10:
    print("Error: la nota debe estar entre 0 y 10.")
elif nota < 3:
    print("Muy Deficiente")
elif nota < 5:
    print("Insuficiente")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:  
    print("Sobresaliente")
