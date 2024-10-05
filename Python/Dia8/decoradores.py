# def cambiarLetras(tipo):
    
#     def mayuscula(texto):
#         print(texto.upper())

#     def minuscula(texto):
#         print(texto.lower())
    
#     if tipo == "mayuscula":
#         return mayuscula
#     elif tipo == "minuscula":
#         return minuscula


# operacion = cambiarLetras("mayuscula")
# operacion("Hola, mundo!")
# operacion("esto es un ejemplo")


# operacion = cambiarLetras("minuscula")
# operacion("Hola, mundo!")
# operacion("ESTO ES UN EjEMPLO")


def decorarSaludo(funcion):
    def otraFuncion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otraFuncion

def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

mayusculaDecorada = decorarSaludo(mayuscula)
mayusculaDecorada("Hola, mundo!")