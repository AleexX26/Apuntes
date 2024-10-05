lista = ["a", "b", "c"]
for letra in lista:
    numeroLetra = lista.index(letra) + 1
    print(f"Letra {numeroLetra}: {letra}")
    

# Ejercicio 2
lista = ["paco", "juan", "pedro", "paco3"]
for nombre in lista:
    if nombre.startswith("j"):
        print(f"Nombre que empieza con 'j': {nombre}")
    else:
        print(f"Nombre que no empieza con 'j': {nombre}")


# Ejercicio 3
numero = [1, 2, 3, 4, 5]
miValor = 0
for numeros in numero:
    miValor = miValor + numeros

print(f"Valor acumulado: {miValor}")


# Ejercicio 4
palabras = "Python"
for letra in palabras:
    print(f"Letra: {letra}")


# Ejercicio 5
for letra in "Python":
    print(f"Letra: {letra}")
    

# Ejercicio 6
for letra in [[1,2], [3,4], [5,6]]:
    print(f"Letra: {letra}")


# Ejercicio 7
for a,b in [[1,2], [3,4], [5,6]]:
    print(f"Primer valor: {a}, Segundo valor: {b}")
    

# Ejercicio 8
dic = {"Clave1": "Valor1", "Clave2": "Valor2", "Clave3": "Valor3"}
for item in dic.items:
    print(item)
    
    

# Ejercicio 9
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        print(f"{numero} es par")
        suma_pares += numero
    else:
        print(f"{numero} es impar")
        suma_impares += numero

print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")
