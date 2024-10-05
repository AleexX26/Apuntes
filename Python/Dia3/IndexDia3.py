miTexto = "Esto es un texto de prueba"

resultado = miTexto[5]
print(f"El caracter en la posición 5 es: {resultado}")

resultado2 = miTexto.index("e")
print(f"El índice de la primera aparición de la letra 'e' es: {resultado2}")

resultado3 = miTexto.index("texto")
print(f"El índice de la primera aparición de la palabra 'texto' es: {resultado3}")

resultado4 = miTexto.index("e", 6)
print(f"El índice de la segunda aparición de la letra 'e' a partir de la posición 6 es: {resultado4}")

resultado5 = miTexto.index("e", 7, 15)
print(f"El índice de la tercera aparición de la letra 'e' a partir de la posición 7 hasta la posición 15 es: {resultado5}")

resultado6 = miTexto.rfind("es")
print(f"El índice de la última aparición de la palabra 'es' es: {resultado2}")