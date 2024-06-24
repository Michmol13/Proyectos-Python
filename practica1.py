numero_de_horas_trabajadas = 0
Costo_por_hora = 0
paga_que_corresponde_por_dia = 0
paga_correspondiente_al_mes = 0

numero_de_horas_trabajadas = int(input("Ingresar_el_numero_de_horas_trabajadas:  "))

Costo_por_hora = int(input("Ingresar_el_Costo_por_hora:  "))

paga_que_corresponde_por_dia = (numero_de_horas_trabajadas * Costo_por_hora)

paga_correspondiente_al_mes = (paga_que_corresponde_por_dia * 30)

print(f"la paga correspondiente por dia es {paga_que_corresponde_por_dia}. \nla paga correspondiente al mes es {paga_correspondiente_al_mes}")