numero_de_payasos = 0
numero_de_muñecas = 0
peso_de_payaso_en_gramos = 112
peso_de_muñeca_en_gramos = 75
peso_total_del_paquete = 0

numero_de_payasos = int(input("Ingrese el número de payasos vendidos: "))

numero_de_muñecas = int(input("Ingrese el número de muñecas vendidos: "))

peso_total_del_paquete = (numero_de_payasos * peso_de_payaso_en_gramos) + (numero_de_muñecas * peso_de_muñeca_en_gramos)

print(f"El peso total del paquete es {peso_total_del_paquete}")