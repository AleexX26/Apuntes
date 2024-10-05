miArhivo = open("Prueba.txt")

print(miArhivo.name)
print(miArhivo.read())

unaLinea = miArhivo.readline()

print(unaLinea)

for l in miArhivo:
    print("Aqui dice: ", l)

todas = miArhivo.readlines()
todas = todas.pop()
print(todas)

miArhivo.close()

