cantidad = int(input("INTRODUCIR Entero cantidad: "))

if cantidad % 5 != 0:
    print("ERROR")
else:
    Billetes500 = cantidad // 500
    cantidad = cantidad % 500

    Billetes200 = cantidad // 200
    cantidad = cantidad % 200

    Billetes100 = cantidad // 100
    cantidad = cantidad % 100

    Billetes50 = cantidad // 50
    cantidad = cantidad % 50

    Billetes20 = cantidad // 20
    cantidad = cantidad % 20

    Billetes10 = cantidad // 10
    cantidad = cantidad % 10

    Billetes5 = cantidad // 5
    cantidad = cantidad % 5

    print("Billetes de 500:", Billetes500)
    print("Billetes de 200:", Billetes200)
    print("Billetes de 100:", Billetes100)
    print("Billetes de 50:", Billetes50)
    print("Billetes de 20:", Billetes20)
    print("Billetes de 10:", Billetes10)
    print("Billetes de 5:", Billetes5)
