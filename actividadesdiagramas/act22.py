#Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos son positivos y cuantos negativos
num =0
neg = 0
pos = 0

while num < 100:
    n = int(input("Ingrese un número : "))
    
    if n == 0:
        print("El número no puede ser cero, intenta de nuevo.")
        continue
    
    if n > 0:
        pos += 1
    else:
        neg += 1
    
    num += 1

print(f"Números positivos: ",pos)
print(f"Números negativos: ",neg)