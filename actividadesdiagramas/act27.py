hay_diez = 0
nota = 0 

while nota != -1:
    nota = int(input("Ingrese una nota (-1 para terminar): "))
    
    if nota == -1:
        break
    elif nota >= 0 and nota <= 10:
        if nota == 10:
            hay_diez += 1
    else:
        print("Nota inválida. Debe estar entre 0 y 10.")
        
if hay_diez == 1:
    print("Sí hubo al menos una nota con valor 10.")
else:
    print("No hubo ninguna nota con valor 10.")