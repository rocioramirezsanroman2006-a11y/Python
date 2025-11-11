#Dibuja un ordinograma de un programa que lea dos números y nos diga cual es mayor o sison iguales
print ("Dime un numero")
num1 = int (input())
print ("Dime otro numero")
num2 = int (input())
if num1==num2:
    print("Los numeros son iguales")
else:
    if num1<num2:
        mayor =num2
    else:
        mayor = num1
    print("El mayor es:", mayor)
