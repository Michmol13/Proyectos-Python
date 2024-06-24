segundos_totales = 0
horas = 0
minutos = 0
segundos_restantes = 0

# Solicitar la cantidad de segundos
segundos_totales = int(input("Ingresa la cantidad de segundos: "))

horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos_restantes = segundos_totales % 60

print(f"{segundos_totales} segundos son {horas} horas, {minutos} minutos y segundos {segundos_restantes}")
