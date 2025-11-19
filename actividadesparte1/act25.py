dado1 = int(input("Ingrese el valor del primer dado (1-6): "))
dado2 = int(input("Ingrese el valor del segundo dado (1-6): "))
dado3 = int(input("Ingrese el valor del tercer dado (1-6): "))
seis_count = 0
if dado1 == 6:
    seis_count += 1
if dado2 == 6:
    seis_count += 1
if dado3 == 6:
    seis_count += 1


match seis_count:
    case 3:
        print("Excelente")
    case 2:
        print("Muy bien")
    case 1:
        print("Regular")
    case 0:
        print("Pésimo")
        
    

            