n = 6 

for i in range(n):
    espacios = "  " * (n - 1 - i)
    
    if i == 0:
        print(espacios + "*")
    else:
        hueco = " " * (i * 2 - 1)
        print(espacios + "*" + hueco + "*")

for i in range(n - 2, -1, -1):
    espacios = "  " * (n - 1 - i)
    
    if i == 0:
        print(espacios + "*")
    else:
        hueco = " " * (i * 2 - 1)
        print(espacios + "*" + hueco + "*")