# Bucle while
contador = 0
print("Bucle while:")
while contador < 5:
    print("El contador es:", contador)
    contador += 1

# Bucle for
print("\nBucle for:")
for i in range(5):
    print("El valor de i es:", i)

################################################################

# Bucle while: Suma de números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_pares = 0
indice = 0

print("Bucle while:")
while indice < len(numeros):
    if numeros[indice] % 2 == 0:  # Verificar si el número es par
        suma_pares += numeros[indice]
    indice += 1

print("La suma de los números pares en la lista es:", suma_pares)

# Bucle for: Productos de números impares
productos_impares = 1

print("\nBucle for:")
for num in numeros:
    if num % 2 != 0:  # Verificar si el número es impar
        productos_impares *= num

print("El producto de los números impares en la lista es:", productos_impares)
