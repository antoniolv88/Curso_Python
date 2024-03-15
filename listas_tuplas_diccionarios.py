# Listas
frutas = ['manzana', 'banana', 'naranja', 'pera', 'kiwi']
print("Lista de frutas:", frutas)

# Tuplas
colores = ('rojo', 'verde', 'azul', 'amarillo', 'morado')
print("Tupla de colores:", colores)

# Diccionarios
persona = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
print("Diccionario de persona:", persona)

# Acceder a elementos de una lista
print("\nPrimera fruta en la lista:", frutas[0])

# Acceder a elementos de una tupla
print("Segundo color en la tupla:", colores[1])

# Acceder a valores de un diccionario
print("Nombre de la persona:", persona['nombre'])

# Actualizar un valor en una lista
frutas[0] = 'sandía'
print("\nLista de frutas actualizada:", frutas)

# Actualizar un valor en un diccionario
persona['edad'] = 35
print("Edad de la persona actualizada:", persona['edad'])

# Agregar un nuevo elemento a una lista
frutas.append('uva')
print("\nLista de frutas con una nueva fruta:", frutas)

# Agregar un nuevo elemento a un diccionario
persona['profesion'] = 'ingeniero'
print("Diccionario de persona con una nueva clave:", persona)
