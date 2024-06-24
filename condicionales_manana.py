# A usted le piden realizar un programa que, recibiendo el día, el mes y el año de la fecha de hoy,
# calcule e imprima la fecha del día de mañana. Vamos a suponer que todos los meses tienen 31 días. 

dia = 0
mes = 0
anho = 0

dia = int(input("Introduzca el día: "))
mes = int(input("Introduzca el mes: "))
anho = int(input("Introduzca el año: "))

#Siempre le vamos a sumar 1 al día de hoy
dia += 1

#Si se pasa de mes, reseteo el día a 1 y avanzo el mes en 1 
if(dia > 31):
    dia = 1
    mes = mes + 1

#Si se pasa de 12 meses, reseteo el mes a 1 y avanzo el año en 1 
if(mes > 12):
    mes = 1
    anho = anho + 1

print(f"la fecha de mañana es {dia}/{mes}/{anho}")

