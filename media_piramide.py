# Solicita al usuario el número de pisos de la pirámide
pisos = int(input("Introduce la cantidad de pisos de la pirámide: "))

# Genera la media pirámide
for i in range(1, pisos + 1):
    # Imprime espacios en blanco y luego asteriscos
    print ('*' * i)
