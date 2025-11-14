'''
Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
incorrecto
'''
print("Simulación de inicio de sesión")
usuario = input("Nombre de usuario: ")
contraseña = input("Contraseña: ")

correct_usuario = "usuario1"
correct_contraseña = "contraseña1"
if usuario == correct_usuario and contraseña == correct_contraseña:
    print("Inicio de sesión correcto")
else:
    print("Nombre de usuario o contraseña incorrecto")