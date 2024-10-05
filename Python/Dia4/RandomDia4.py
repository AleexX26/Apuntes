from random import *

aleatorio = randint(1, 50)
print(aleatorio)

aleatorio = round(uniform(1, 50),1)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ["rojo", "azul", "amarillo", "verde", "negro"]
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(1, 51, 5))
shuffle(numeros)
print(numeros)

# Ejercicio 2
