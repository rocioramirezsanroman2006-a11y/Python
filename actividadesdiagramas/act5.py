import math

print ("Dame el radio del cuadrado")
radio = int(input())
d = 2 * radio
l = math.pi * d 
a = math.pi * radio**2
vol= (4/3) * math.pi * radio**3
print ("La longuitud de la circunferencia es", l )
print ("El area de la circunferencia es", a )
print ("El voluemn de la esfera es", vol )