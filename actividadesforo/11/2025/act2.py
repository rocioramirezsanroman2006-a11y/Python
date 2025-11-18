n = int(input("Altura: "))

for i in range(n):
    if i == 0:
        print("4")
    elif i == n - 1:
        print("4 " * n)
    else:
        espacio = " " * i
        print("4" + espacio + "4")