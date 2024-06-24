examen1 = 0
examen2 = 0
examen3 = 0
ponderacion = 0 

examen1 = int(input("solicitar_la_nota_de_examen1:  "))
examen2 = int(input("solicitar_la_nota_de_examen2:  "))
examen3 = int(input("solicitar_la_nota_de_examen3:  "))

ponderacion = (examen1 + examen2 + examen3) /3

print (f"la ponderacion es {ponderacion}")