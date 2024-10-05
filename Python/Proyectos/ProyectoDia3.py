texto = input("Ingrese un texto: ")
texto = texto.lower()
letras = []

letras.append(input("Ingrese una letra a agregar: ").lower())
letras.append(input("Ingrese una letra a agregar: ").lower())
letras.append(input("Ingrese una letra a agregar: ").lower())

print("\n")

print("Cantidad de letras: ")
canitdadLetras1 = texto.count(letras[0])
canitdadLetras2 = texto.count(letras[1])
canitdadLetras3 = texto.count(letras[2])

print(f"Hemos encotrado la letra '" + letras[0] + "' " + str(canitdadLetras1) + " veces")
print(f"Hemos encotrado la letra '" + letras[1] + "' " + str(canitdadLetras2) + " veces")
print(f"Hemos encotrado la letra '" + letras[2] + "' " + str(canitdadLetras3) + " veces")

textoReverse = texto[::-1]
print("Texto al revés: " + textoReverse)

buscarPython = texto.find("python")
print(buscarPython)

primeraLetra = texto[0]
ultimaLetra = texto[-1]

print("Primera letra: " + primeraLetra)
print("Ultima letra: " + ultimaLetra)