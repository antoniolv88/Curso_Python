#Formula
#Grados Fahrenheit = (grados centígrados × 9/5) +32
#Preguntarle al usuario que conversion quiere
print("Que conversion quieres hacer?")
print("Celsius a Fah pulsa 1")
print("Fah a Celsius pulsa 2")
conversion_user = int(input("Intoduce una opcion: "))

if conversion_user == 1: 
    #Introducir grados C para convertirlos en Fahrenheit
    grados_centigrados = int(input("Introduce los grados centigrados: "))

    grados_Fahrenheit = (grados_centigrados * 9/5) +32

    print(f"Los {grados_centigrados} ºC son {grados_Fahrenheit} Fahrenheit")
else:
    #Introducir grados F
    grados_Fahrenheit = int(input("Introduce los grados F: "))

    grados_centigrados = (grados_Fahrenheit -32) *5/9

    print(f"Los {grados_Fahrenheit} F son {grados_centigrados} C")