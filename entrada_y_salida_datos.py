# Entrada de datos
nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))  # Convertimos la entrada a un entero

# Salida de datos
print("\n¡Hola,", nombre + "!")  # Concatenamos el nombre con el mensaje
print("Tu edad es:", edad)

# Realizar cálculos con los datos ingresados
anio_actual = 2024
anio_nacimiento = anio_actual - edad
print("Naciste aproximadamente en el año:", anio_nacimiento)
