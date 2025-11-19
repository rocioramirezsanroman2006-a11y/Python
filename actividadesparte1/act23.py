
valor_compra = float(input("Ingrese el valor de compra: "))
metodo_pago = input("Ingrese el método de pago (contado/tarjeta): ")

if metodo_pago == "contado":
    descuento = valor_compra * 0.05
    total_a_pagar = valor_compra - descuento
    print(f"Descuento aplicado: {descuento:}€")
    
elif metodo_pago == "tarjeta":
    recargo = valor_compra * 0.03
    total_a_pagar = valor_compra + recargo
    print(f"Recargo aplicado: {recargo:}€")
    
else:
    print("Método de pago no válido.")
    total_a_pagar = valor_compra 
print(f"Total a pagar: {total_a_pagar:}€")
