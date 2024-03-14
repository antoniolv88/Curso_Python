
#slicing (rebanar o cortar en rebanadas)
texto = "ABCDEFGHIJKLM"
fragmento= texto[2:10:2]
print(fragmento)

#Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
frase = "Controlar la complejidad es la esencia de la programación"
fragmento = frase[0:9]
print(fragmento)

#oma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
frase= "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento = frase[8::3]
print(fragmento)

#Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento = frase[::-1]
print(fragmento)