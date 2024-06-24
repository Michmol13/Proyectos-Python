import math


radio = 0.0
altura = 0.0
volumen = 0.0

# Solicitar el radio y la altura del cilindro
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

# Calcular el volumen del cilindro
volumen = (math.pi * radio ** 2 * altura)

print(f"El volumen del cilindro es {volumen}")