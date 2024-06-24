# Escribe un programa que lea 5 números introducidos por el usuario

# Leer los 5 números del usuario y almacenarlos en una lista
numeros = []
for _ in range(5):
    numero = int(input("Introduce un número: "))
    numeros.append(numero)

# Encontrar el número más grande sin usar métodos de listas
numero_mas_grande = numeros[0]
for numero in numeros:
    if numero > numero_mas_grande:
        numero_mas_grande = numero

# Imprimir el número más grande
print("El número más grande es:", numero_mas_grande)
