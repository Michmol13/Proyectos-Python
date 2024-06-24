import random

# Solicita al usuario el número de pisos de la pirámide
num_pisos = int(input("Introduce la cantidad de pisos de la pirámide: "))

# Rango de caracteres ASCII deseado (puedes ajustar este rango)
ascii_start = 33
ascii_end = 44 

# Genera la pirámide completa
for i in range(1, num_pisos + 1):
    # Selecciona un carácter ASCII aleatorio dentro del rango especificado
    char = chr(random.randint(ascii_start, ascii_end))
    # Imprime los espacios en blanco
    print(' ' * (num_pisos - i), end='')
    # Imprime los caracteres ASCII
    print(char * (2 * i - 1))