edad = 0

edad = int(input("Ingresar la edad del usuario: "))

if(edad >= 18):
    print("Puede pasar") #Esta linea solo se ejecuto si el if tiene un verdadero
elif(edad >= 12):
    print("Puede pasar acompañado de un adulto")
elif(edad < 12):
    print("Menor de edad No puede pasar")