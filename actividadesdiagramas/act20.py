print("Escribe un numero")
n = int(input())
fac = 1
for i in range (1,n+1):
    fac = fac*i
    print("El factorial de", n, "es", fac)