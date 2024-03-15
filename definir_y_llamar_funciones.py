# Definición de una función para calcular el área de un círculo
def calcular_area_circulo(radio):
    pi = 3.14159
    area = pi * radio ** 2
    return area

# Llamada a la función
radio = 5
area_del_circulo = calcular_area_circulo(radio)
print("El área del círculo con radio", radio, "es:", area_del_circulo)

# Definición de una función para saludar a una persona que toma dos parámetros

def saludar(nombre, edad):
    print("¡Hola,", nombre + "! Tienes", edad, "años.")

# Llamada a la función con argumentos específicos
saludar("Juan", 30)

# Llamada a la función con otros argumentos
saludar("María", 25)

# Llamada a la función con variables como argumentos
nombre = "Pedro"
edad = 35
saludar(nombre, edad)
