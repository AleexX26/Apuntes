texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

fragmento = texto[2]
print(f"El fragmento de la letra es: {fragmento}")

fragmento2 = texto[4:10]
print(f"El fragmento de las letras es: {fragmento2}")

fragmento3 = texto[2:10:2]
print(f"El fragmento de las letras con salto es: {fragmento3}")

fragmento4 = texto[::-1]
print(f"El fragmento de las letras al revés es: {fragmento4}")

fragmento5 = texto[::-2]
print(f"El fragmento de las letras al revés con salto es: {fragmento5}")

fragmento6 = texto[::3]
print(f"El fragmento de las letras con salto de 3 es: {fragmento6}")

fragmento7 = texto[5:]
print(f"El fragmento de las letras desde la letra 5 es: {fragmento7}")

fragmento8 = texto[:5]
print(f"El fragmento de las letras hasta la letra 5 es: {fragmento8}")

fragmento9 = texto[5:10]
print(f"El fragmento de las letras desde la letra 5 hasta la letra 10 es: {fragmento9}")

fragmento10 = texto[10:5:-1]
print(f"El fragmento de las letras desde la letra 10 hasta la letra 5 al revés es: {fragmento10}")

fragmento11 = texto[10:5:-2]
print(f"El fragmento de las letras desde la letra 10 hasta la letra 5 al revés con salto de 2 es: {fragmento11}")

fragmento12 = texto[10::-1]
print(f"El fragmento de las letras desde la letra 10 al revés es: {fragmento12}")

fragmento13 = texto[10::-2]
print(f"El fragmento de las letras desde la letra 10 al revés con salto de 2 es: {fragmento13}")