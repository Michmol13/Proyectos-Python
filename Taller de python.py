#programa que le pida al usuario su nombre y edad menos 5 años 
 # nombre del usuario
nombre = input("¿Cuál es tu nombre? ")

 # edad del usuario
edad = int(input("¿Cuántos años tienes? "))

 # Restar 5 años a la edad
nueva_edad = edad - 5

 # Imprimir un mensaje con la nueva edad
print(f"{nombre}, si restamos 5 años a tu edad, tendrías {nueva_edad} años.")
