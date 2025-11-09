#Dibuja un ordinograma de un programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos
num= 0
neg = 0
pos = 0

while True:
    n = int(input("Ingrese un número: "))
    if n == 0:
        break
    if n > 0:
        pos += 1
    else:
        neg += 1
        
print(f"Números positivos: ",pos)
print(f"Números negativos: ",neg)