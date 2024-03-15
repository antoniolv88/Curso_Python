"""
creamos una función llamada dividir que toma dos números como argumentos y trata de dividir el primer número por el segundo. Dentro del bloque try, intentamos realizar la división. Si se produce una excepción de tipo ZeroDivisionError (división por cero), capturamos esta excepción dentro del bloque except y mostramos un mensaje de error. El bloque finally se ejecuta siempre, independientemente de si se produce una excepción o no. En este caso, simplemente imprimimos un mensaje indicando que se ejecutó el bloque finally.
Al ejecutar este código, si intentamos dividir un número por cero, se capturará la excepción y se imprimirá un mensaje de error. Sin embargo, el bloque finally siempre se ejecutará, independientemente de si se produce una excepción o no. Esto es útil para realizar tareas de limpieza, como cerrar archivos o conexiones de red, después de que se complete el bloque try o except.
"""

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None
    finally:
        print("Se ejecutó el bloque finally.")

# Ejemplo de uso
num1 = 10
num2 = 0

resultado = dividir(num1, num2)
if resultado is not None:
    print("El resultado de la división es:", resultado)
else:
    print("No se pudo realizar la división debido a un error.")

