# Definición de una función para calcular el área de un círculo
def calcular_area_circulo(radio):
    pi = 3.14159
    area = pi * radio ** 2
    return area

# Llamada a la función
radio = 5
area_del_circulo = calcular_area_circulo(radio)
print("El área del círculo con radio", radio, "es:", area_del_circulo)

# Definición de una función para saludar a una persona
def saludar(nombre):
    print("¡Hola,", nombre + "! ¿Cómo estás?")

# Llamada a la función
nombre = "Juan"
saludar(nombre)
