# INICIO
MIN = 1
MAX = 100
BAND = False

print("PIENSA UN NÚMERO DEL 1 AL 100")

while BAND == False:
    NUM = (MIN + MAX) // 2  
    print("¿Tu número es?",NUM)
    
    OPINION = input("Responde con 'mayor', 'menor' o 'igual': ")
    if OPINION == 'mayor':
        MIN = NUM + 1
    elif OPINION == 'menor':
        MAX = NUM - 1
    elif OPINION == 'igual':
        BAND = True
        print("¡ADIVINÉ!")
    else:
        print("Respuesta no válida. Escribe 'mayor', 'menor' o 'igual'.")
