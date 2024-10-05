"""
def chequear3Cifras(numero):
    return numero in range(100, 1000)

suma = 586 + 402

resultado = chequear3Cifras(suma)
print(resultado)

def chequear(lista):
    
    lista3 = []
    for n in lista:
        if n in range(100,1000):
            lista3.append(n)
        else:
            pass
        
    return lista3

resultado = chequear([586, 402, 123, 999, 88])
print(resultado)


def todos_positivos(lista):
  for numero in lista:
    if numero < 0:
      return False
  return True

lista_numeros = [5, -3, 3]
resultado = todos_positivos(lista_numeros)
print(resultado)


def sumar_menores(lista):
    
    lista_numeros = []
    for n in lista:
        if n in range(0,1000):
            lista_numeros.append(n)
        else:
            pass
        
    return lista_numeros

resultado = sumar_menores([5 + 5])
print(resultado)

"""


def cantidad_pares():
    lista_numeros = []
    for n in range(100, 1000):  # Assuming we want to check for 3-digit numbers
        if n % 2 == 0:
            lista_numeros.append(n)
    return lista_numeros

# Calculate the average of the even numbers
def promedio_pares():
    lista_pares = cantidad_pares()
    if lista_pares:
        promedio = sum(lista_pares) / len(lista_pares)
        print(promedio)
    else:
        print("No hay números pares en el rango.")

promedio_pares()