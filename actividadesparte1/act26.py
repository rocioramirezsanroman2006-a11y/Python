d1 = int(input("Primer dado: "))
d2 = int(input("Segundo dado: "))
d3 = int(input("Tercer dado: "))

contador_seis = 0

if d1 == 6:
    contador_seis += 1
if d2 == 6:
    contador_seis += 1
if d3 == 6:
    contador_seis += 1

match contador_seis:
    case 3:
        print("Excelente")
    case 2:
        print("Muy bien")
    case 1:
        print("Regular")
    case 0:
        print("Pésimo")
