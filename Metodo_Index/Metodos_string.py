"""Metodos:
    upper() - pasar a mayusculas
    lower() - pasar a minúsculas
    split() - separalo en partes(listas)
    join() - unir items usando separador
    find() - encontrar un sub-string
    replace() -reemplazar un substring    
   """

texto = "Este es el texto de Antonio"
resultado = texto.replace("e", "x" )
print(resultado)

"""
b="Python"
c= "es"
d="genial"
e=" ".join([a,b,c,d])
print(e)
"""
#Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
resultado=frase.upper()
print(resultado)

#Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
e=" ".join(lista_palabras)
print(e)

"""Reemplaza en la siguiente frase:
"Si la implementación es difícil de explicar, puede que sea una mala idea."
los siguientes pares de palabras:
"difícil" --> "fácil"
"mala" --> "buena"
y muestra en pantalla la frase con ambas palabras modificadas.
    """
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
remplazar = frase.replace("difícil","fácil")
remplazar = frase.replace("mala","buena")

print(remplazar)