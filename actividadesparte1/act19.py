'''
Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
con el siguiente menú de opciones:
Bienvenido a su Cajero Virtual
1. Ingresar dinero en cuenta
2. Retirar dinero de la cuenta
3. Salir
'''
saldoinicial = 1000
saldo = saldoinicial
print("Bienvenido a su Cajero Virtual")
print("1. Ingresar dinero en cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Salir")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    saldo += cantidad   
    print(f"Saldo actual: {saldo}")

elif opcion == "2":
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    if cantidad <= saldo:
        saldo -= cantidad
        print(f"Saldo actual: {saldo}")
    else:
        print("Saldo insuficiente")
        
elif opcion == "3":
    print("Gracias por usar el Cajero Virtual. ¡Hasta luego!")
    exit()  
    
else :
    print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
   