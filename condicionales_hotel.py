# Haga un programa que calcule la cuenta de un cliente que se hospeda una cierta cantidad de noches en un hotel.
# El costo por noche es definido por el usuario:
# •Si el cliente se hospeda más de 4 noches se le hace un descuento del 15%
# •En caso contrario el descuento es de 5%

noches_hospedaje = 0 
costo_noche = 0 
descuento_premium = 0.15
descuento_regular = 0.05
costo_total = 0

noches_hospedaje = int(input("Ingrese la cantidad de noches: "))
costo_noche = float(input("Ingrese el costo por noche: "))

if noches_hospedaje > 4: 
    costo_total =noches_hospedaje*costo_total*(1 - descuento_premium)
else: 
    costo_total = noches_hospedaje*costo_noche*(1- descuento_regular)

print(f"El costo total es de {costo_total:.2f} CRC")
