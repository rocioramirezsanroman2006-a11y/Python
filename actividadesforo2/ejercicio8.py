'''Ejercicio 8: Rombo sólido
Enunciado:

Imprime un rombo sólido de altura 2n-1, centrado, usando asteriscos.

Figura para n=4:'''
altura= int(input("Introduce la altura del diamante : "))
n = altura
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i -1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i -1))