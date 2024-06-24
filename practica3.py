precio_normal_de_la_barra_de_pan = 1500
porcentaje_de_descuento = 60
precio_con_descuento = 0
numero_de_barras_que_no_son_del_dia = 0
costo_total = 0

numero_de_barras_que_no_son_del_dia = int(input("Ingresar la cantidad de pan que no sea del dia: "))

precio_con_descuento = (porcentaje_de_descuento / 100 * precio_normal_de_la_barra_de_pan)

costo_total = numero_de_barras_que_no_son_del_dia * precio_con_descuento

print(f"El precio con descuento es {precio_con_descuento}. \nel costo total es {costo_total}.")