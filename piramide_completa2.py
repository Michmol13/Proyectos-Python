# Solicita al usuario el número de pisos de la pirámide
num_pisos = int(input("Introduce la cantidad de pisos de la pirámide: "))

# Genera la pirámide completa
for i in range(1, num_pisos + 1):
    # Imprime los espacios en blanco
    print(' ' * (num_pisos - i) + '*' * (2 * i - 1))