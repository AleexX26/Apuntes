# Práctica Métodos y Ayuda 1

print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))
# Práctica Métodos y Ayuda 2

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3,"naranja")
# Práctica Métodos y Ayuda 3

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
 
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
 
conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
# Práctica Crear Funciones 1

def saludar():
    print("¡Hola mundo!")
# Práctica Crear Funciones 2

nombre_persona = "Luis"
 
def bienvenida(nombre_persona):
    print(f'¡Bienvenido {nombre_persona}!')
# Práctica Crear Funciones 3

un_numero = 5
 
def cuadrado(un_numero):
    print(un_numero**2)
# Práctica Return 1

def potencia(num1, num2):
    return num1**num2
# Práctica Return 2

dolares = 1200
 
def usd_a_eur(dolares):
    return dolares*0.90
# Práctica Return 3

palabra = "Curso de Python"
 
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra
# Práctica Funciones Dinámicas 1

lista_numeros = [1,-50,502,-5000,755,600,33,61]
 
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True
# Práctica Funciones Dinámicas 2

lista_numeros = [1,50,500,5000,750,600]
 
def suma_menores(lista_numeros):
    suma=0
    for numero in lista_numeros:
        if numero in range(1,1000):
            suma += numero
        else:
            pass
    return suma
# Práctica Funciones Dinámicas 3

lista_numeros = [1,50,502,5000,755,600,33,61]
 
def cantidad_pares(lista_numeros):
    cantidad=0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad
# Práctica sobre Interacción entre Funciones 1

import random
 
def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)
 
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
# Práctica sobre Interacción entre Funciones 2

lista_numeros = [1,2,15,7,2,8]
 
def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista
 
def promedio(lista):
    valor_medio = sum(lista)/len(lista)
    return valor_medio
# Práctica sobre Interacción entre Funciones 3

lista_numeros = [1,2,15,7,2,8]
 
import random
 
def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado
 
def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista
# Práctica sobre Argumentos Indefinidos (*args) 1

def suma_cuadrados(*args):
    suma = 0
    for arg in args:
        suma += arg**2
    
    return suma
# Práctica sobre Argumentos Indefinidos (*args) 2

def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)
    
    return suma
# Práctica sobre Argumentos Indefinidos (*args) 3

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'
# Práctica sobre Argumentos Indefinidos (*kwargs) 1

def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad
# Práctica sobre Argumentos Indefinidos (*kwargs) 2

def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista
# Práctica sobre Argumentos Indefinidos (*kwargs) 3

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')