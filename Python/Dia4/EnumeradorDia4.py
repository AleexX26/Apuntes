lista = ["a", "b", "c"]

for indice, item in enumerate(lista):
    print(indice, item)

# Ejercicio 2
lista = ["a", "b", "c", "d", "e"]
tuples = list(enumerate(lista))
print(tuples[1][0])

# Ejercicio 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


# Ejercicio 4
tuples = list(enumerate("Python"))
print(tuples)

# Ejercicio 5
# Lista de nombres
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Recorremos la lista usando enumerate() para obtener tanto el índice como el nombre
for indice, nombre in enumerate(lista_nombres):
    # Comprobamos si el nombre empieza con 'M'
    if nombre.startswith('M'):
        print(indice)  # Imprime el índice del nombre que empieza con 'M'
