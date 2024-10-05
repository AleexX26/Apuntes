texto = "Esto es un texto de prueba"

resultado = texto
print(f"Texto original: {texto}")

resultado2 = texto.upper()
print(f"Texto en mayúsculas: {resultado2}")

resultado2 = texto[2].upper()
print(f"Texto en mayúsculas: {resultado2}")

resultado2 = texto.lower()
print(f"Texto en minúsculas: {resultado2}")

resultado2 = texto.split()
print(f"Texto separado por espacios: {resultado2}")

a = "a"
b = "b"
c = "c"
d = "d"
e = " ".join([a, b, c, d])
print(f"Texto concatenado: {e}")

resultado2 = texto.find("t")
print(f"Posición de la primera 't': {resultado2}")

resultado2 = texto.replace("e", "o").replace("u", "i")
print(f"Texto reemplazado: {resultado2}")


