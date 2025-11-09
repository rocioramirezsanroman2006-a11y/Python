pares = 0
impares = 0
i = 100

while i <= 200:
    if i % 2 == 0:
        pares += i
    else:
        impares += i
    i += 1

print("Suma de pares:", pares)
print("Suma de impares:", impares)
