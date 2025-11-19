while True:
    try:
        horas = int(input("Ingrese las horas (0-23): "))
        minutos = int(input("Ingrese los minutos (0-59): "))
        segundos = int(input("Ingrese los segundos (0-59): "))

        if 0 <= horas < 24 and 0 <= minutos < 60 and 0 <= segundos < 60:
            break
        else:
            print("Por favor, ingrese una hora válida.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros.")
segundos += 1
if segundos == 60:
    segundos = 0
    minutos += 1
    if minutos == 60:
        minutos = 0
        horas += 1
        if horas == 24:
            horas = 0
print(f"La hora después de un segundo es: {horas:}:{minutos:}:{segundos:}")