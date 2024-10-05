for numero in range(5):
    print(numero)

#Ejercicio 2
for numero in range(1, 6):
    print(numero)

#Ejercicio 3
for numero in range(1, 11, 2):
    print(numero)

#Ejercicio 4
for numero in range(10, 0, -1):
    print(numero)
    
#Ejercicio 5
lista = list(range(1, 101))
for numero in lista:
    print(numero)
    

#Ejercicio 6
# Inicializamos la variable para acumular la suma de los cuadrados
suma_cuadrados = 0

# Usamos un rango de 1 a 15 (inclusive)
for numero in range(1, 16):  # El 16 no está incluido, por lo tanto llegará hasta 15
    cuadrado = numero ** 2  # Calculamos el cuadrado de cada número
    suma_cuadrados += cuadrado  # Acumulamos el cuadrado en suma_cuadrados

# Mostramos el resultado final
print("La suma de los cuadrados del 1 al 15 es:", suma_cuadrados)
