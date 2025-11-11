print("Dame un numero")
num1 = int (input())
print("Dame otro numero")
num2 = int (input())
suma = num1 + num2
print("La suma es: ", suma)
resta = num1 - num2 
print("La resta es: ", resta)
multiplicacion = num1 * num2
print("La multiplicacion es: ", multiplicacion)

if (num2 == 0):
    print("No es posible dividir entro 0")
else:
    division = num1 / num2
    print("Resultado de la division", division)
    