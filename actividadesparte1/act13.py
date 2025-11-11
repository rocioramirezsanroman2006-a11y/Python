#Dibuja un ordinograma de un programa que lea dos números y lo visualiza en ordenascendente
print ("Dime un numero")
num1 = int (input())
print ("Dime otro numero")
num2 = int (input())
if num1>num2 :
    print (num1,"<",num2)
else :
    print (num2,"<",num1)