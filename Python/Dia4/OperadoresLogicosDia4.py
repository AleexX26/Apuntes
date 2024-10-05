4 < 5
5 > 6
5 == 5
5 != 6
miBool = (4 < 5) and (5 > 6)
print(miBool) # False

miBool = 1 == 10 or 3 == 3
print(miBool) # True

texto = "Esta frase en breve"

miBool = ("breve" in texto) and ("hola" in texto)
print(miBool) # True

miBool = not "a" == "a"
print(miBool) # False