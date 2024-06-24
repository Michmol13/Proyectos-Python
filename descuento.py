precio_noche = 100
cantidad_noches = 0
porc_descuento = 0.05
subtotal = 0
descuento = 0 
total = 0 

cantidad_noches = int(input("ingrese la cantidad de noches"))

subtotal = cantidad_noches * precio_noche

descuento = subtotal * porc_descuento

total = subtotal - descuento

print (f'El total es {total} USD')