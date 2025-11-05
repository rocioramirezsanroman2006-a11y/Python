print ("Introduce el precio de venta")
pventa = int(input())
print ("Introduce el precio del articulo")
particulo = int(input())
descuento = 100 - (pventa * 100) / particulo
print ("El descuento es : ", descuento)
