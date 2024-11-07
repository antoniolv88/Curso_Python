#comparar numero
import random

#Generar un numero random
num_aleatorio= random.randrange(0,10)
print(f"El num aleatorio es: {num_aleatorio}")

#Pedir al usuario que introduzca un numero
num_usuario= int(input("Adivina un numero entre 1 y 10:"))
#print(f"El numero introducido es: {num_usuario}")
#Comprobar los numero
while num_usuario != num_aleatorio:
    if num_usuario > num_aleatorio:
        print("El numero introducido por el usuario es mayor que el aleatorio")
    else:
        print("El numero introducido por el usuario es menor")
    
    num_usuario=int(input("Introduce otro numero:"))

print("Has acertado")
    
    

#indicar si es mayor o menor