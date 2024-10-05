def multiplicar(a, b):
    return a * b

resultado = multiplicar(5, 3)
print(f"El resultado de la multiplicación es: {resultado}")



def potencia(base, exponente):
  resultado = base ** exponente
  return resultado


def usd_a_eur(dolares):

  tasa_de_cambio = 0.90

  euros = dolares * tasa_de_cambio

  return euros

dolares = 100

euros_resultante = usd_a_eur(dolares)

print(f"{dolares} dólares equivalen a {euros_resultante} euros.")

def invertir_palabra(palabra):

  palabra_invertida = palabra[::-1]
  palabra_mayuscula = palabra_invertida.upper()
  return palabra_mayuscula

palabra = "Python"
resultado = invertir_palabra(palabra)
print(resultado)  