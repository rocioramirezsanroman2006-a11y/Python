'''Imprime un diamante hueco de altura total 2n - 1, centrado con asteriscos, 
donde solo se imprimen los bordes y el centro.'''
altura = int (input("Introduce la altura del triangulo:"))
n = altura
for i in range(n):
    print((n - 1 - i) * " " , end="")
    if i == 0:
        print("*")
    else:
        espacio = " " * (i * 2 - 1)
        print("*" + espacio + "*")
    
for i in range(n - 2, -1, -1):
    print((n - 1 - i) * " " , end="")
    if i == 0:
        print("*")
    else:
        espacio = " " * (i * 2 - 1)
        print("*" + espacio + "*")