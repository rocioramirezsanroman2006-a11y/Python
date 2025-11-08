CONT = 1
NEG_FOUND = 0

while CONT <= 10:
    print("Escribe un numero")
    num= int (input())
    if num == 0:
        print ("Error.No introduzca 0")
    else:
        if num < 0: 
            NEG_FOUND = 1
        CONT = CONT + 1

if NEG_FOUND == 1:
    print("Se introdujo al menos un numero negativo.")
else:
    print("No se introdujeron numeros negativos.")
