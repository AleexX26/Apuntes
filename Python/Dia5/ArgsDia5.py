def suma(a,b):
    return a + b
print(suma(2, 3))

def multiplica(*args): # Variable number of arguments con * es todos lo que se pasan como argumentos
    total = 0
    
    for arg in args:
        total *= arg
    
    return total
print(multiplica(2, 3, 4, 5))

def suma_cuadrados(*args):
    total= 0
    for arg in args:
        total += arg
        
    return total

print(suma_cuadrados(1,4,9))

def suma_absolutos(*args):
    total = 0
    
    for suma in args:
        total += abs(suma)
    return total
    
print(suma_absolutos(2,3,5,-7))
        

def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    return f"{nombre}, la suma de tus números es {suma_numeros}"

# Ejemplo de uso:
resultado = numeros_persona("Ana", 1, 2, 3, 4)
print(resultado)
