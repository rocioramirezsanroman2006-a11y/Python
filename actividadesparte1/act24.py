monto_compra = float(input("Ingrese el monto de la compra: "))
dia_semana = input("Ingrese el día de la semana: ").lower()
if dia_semana == "martes" or dia_semana == "jueves":
    descuento = monto_compra * 0.15
    total_a_pagar = monto_compra - descuento
    print(f"Descuento aplicado: {descuento:}€")
else:
    total_a_pagar = monto_compra
    print("No se aplicó ningún descuento.")
print(f"Total a pagar: {total_a_pagar:}€")


