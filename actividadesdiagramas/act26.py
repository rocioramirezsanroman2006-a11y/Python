empleado = str(input("Dime tu nombre: "))
pago_hora = int(input("Dime el salario bruto por hora del trabajador: "))
horas = int(input("Dime las horas trabajadas en la semana: "))

if horas > 35:
    sueldo_bruto = (35 * pago_hora) + ((horas - 35) * pago_hora * 1.5)
else:
    sueldo_bruto = horas * pago_hora

if sueldo_bruto <= 500:
    impuestos = 0
    sueldo_neto = sueldo_bruto
elif sueldo_bruto <= 900:
    impuestos = (sueldo_bruto - 500) * 0.25
    sueldo_neto = sueldo_bruto - impuestos
else:
    impuestos = (400 * 0.25) + ((sueldo_bruto - 900) * 0.45)
    sueldo_neto = sueldo_bruto - impuestos

print("\nEmpleado: ", empleado)
print("Sueldo bruto: ", sueldo_bruto, "€")
print("Impuestos aplicados: ", impuestos, "€")
print("Sueldo neto: ", sueldo_neto, "€")
