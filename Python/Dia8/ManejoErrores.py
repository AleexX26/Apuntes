# def suma():
#     n1 = int(input("Ingrese el primer número: "))
#     n2 = int(input("Ingrese el segundo número: "))
#     print(n1+n2)
#     print("Gracias por sumar" + n1)






# try:
#     # Codigo que queremos probar
#     suma()
# except:
#     # Codigo a ejecutar si se produce una excepcion
#     print("Hubo un error en la suma")
# else:
#     # Codigo que se ejecuta si no se produce una excepcion
#     print("La suma se realizó correctamente")

# finally:
#     # Codigo que siempre se ejecuta
#     print("Ejecución finalizada")




# try:
#     # Codigo que queremos probar
#     suma()
# except TypeError:
#     # Codigo a ejecutar si se produce una excepcion
#     print("Estas intentando concaternar tipos distintos ")
# except ValueError:
#     print("Ese no es un numero")
# else:
#     # Codigo que se ejecuta si no se produce una excepcion
#     print("La suma se realizó correctamente")
# finally:
#     # Codigo que siempre se ejecuta
#     print("Ejecución finalizada")

# --------------------------------------------------------------------

#Ejercicio 2
def pedirNumero():
    
    while True:
        try:
            numero = int(input("Ingrese un número: "))
        except ValueError:
            print("Error, ingrese un número válido.")
        else:
            print(f"El número ingresado es: {numero}")
            break
    print("gracias")
pedirNumero()