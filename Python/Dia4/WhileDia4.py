monedas = 5

while monedas > 0:
    print(f"Te quedan {monedas} monedas.")
    monedas -= 1

print("Has gastado todas las monedas.")

# Ejercicio 2
respuestas = "s"
while respuestas == "s":
    respuesta = input("¿Deseas continuar? (s/n): ")
else:
    print("Gracias por participar.")
    

# Ejercicio 3
nombre = input("Ingresa tu nombre: ")

for letra in nombre:
    if letra == "r":
        break
    print(letra)
    
# Ejercicio 4
nombre = input("Ingresa tu nombre: ")

for letra in nombre:
    if letra == "r":
        continue
    print(letra)
    

# Ejercicio 5
numero = 50
while numero >= 0:  # Incluye el número 0
    if numero % 5 == 0:  # Si es divisible por 5
        print(numero)
    numero -= 1  # Resta 1 en cada iteración para evitar un bucle infinito
