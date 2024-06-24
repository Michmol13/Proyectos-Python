# Escribe un programa que lea 5 números introducidos por el usuario

# Leer los 5 números del usuario y almacenarlos en una lista
numeros = []
for _ in range(7):
    numero = int(input("Introduce un número: "))
    numeros.append(numero)

# Encontrar el número más grande usando el método max()
numero_mas_grande = max(numeros)

# Imprimir el número más grande
print("El número más grande es:", numero_mas_grande)