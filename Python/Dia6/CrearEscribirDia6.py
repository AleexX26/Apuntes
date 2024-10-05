archivo = open("Pruba1.txt", "r")
archivo = open("Pruba1.txt", "w")
archivo = open("Pruba1.txt", "a")

archivo.write("Esto es una prueba\n")
archivo.writelines(["Segunda línea\n", "Tercera línea\n"])

lista = ["Cuarta línea\n", "Quinta línea\n"]
for p in lista:
    archivo.writelines(p)

archivo.close()