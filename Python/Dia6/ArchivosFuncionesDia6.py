archivo = open("Prueba.txt")

def abrir_leer():
    print(archivo.read())
    return archivo


def sobrescribir():
    archivo = open("Prueba.txt", "w")
    archivo.write("Esto es una prueba sobreescrita\n")
    print(archivo.read())
    return archivo


# abrir_leer()
sobrescribir()



archivo.close()