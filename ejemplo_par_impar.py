#Aca inicia mi programa
numero = int(input("Ingrese el numero: "))

#Operacion "modulo" que me retorna el residuo
#Calculo el modulo del numero
residuo = (numero%2)

#Si el modulo(residuo) es 0, el numero es par. Si no, es impar. 
if(residuo == 0 ):
    print('El numero es par')
else:
    print('El numero es impar')