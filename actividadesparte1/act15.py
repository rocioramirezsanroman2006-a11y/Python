#Dibuja un ordinograma de un programa que lea tres números y nos diga cual es mayor, cual es menor y cuales son iguales
print("Dime un numero")
num1 = int (input())
print ("Dime otro numero")
num2 = int (input())
print ("Dime le ultimo numero")
num3 = int (input())

if num1 == num2 and num2==num3:
    print ("Los numeros son iguales")
else :
    if num1 > num2 and num1 >num3:
        mayor = num1
        print("El mayor es:", mayor)
    elif num2 > num1 and num2 >num3:
        mayor =num2 
        print("El mayor es:", mayor)
    else :
        mayor = num3
        print("El mayor es:", mayor)
    
    
    if num1 < num2 and num1 <num3:
        menor = num1
        print("El menor es:", menor)
    elif num2 < num1 and num2 <num3:
        menor =num2
        print("El menor es:", menor)
    else :
        menor = num3
        print("El menor es:", menor)
        
