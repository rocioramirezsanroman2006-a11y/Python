horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))
tarifa_normal = float(input("Ingrese la tarifa normal por hora: "))

if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * tarifa_normal
else:
    horas_extra = horas_trabajadas - 35
    salario_bruto = (35 * tarifa_normal) + (horas_extra * tarifa_normal * 1.5)  
    
if salario_bruto <= 500:
    impuesto = 0
elif salario_bruto <= 900:
    impuesto = (salario_bruto - 500) * 0.25
else:
    impuesto = (400 * 0.25) + ((salario_bruto - 900) * 0.45)
salario_neto = salario_bruto - impuesto
nombre_trabajador = input("Ingrese el nombre del trabajador: ")
print(f"Nombre del trabajador: {nombre_trabajador}")
print(f"Salario bruto: {salario_bruto:}€")
print(f"Tasas: {impuesto:}€")
print(f"Salario neto: {salario_neto:}€")

