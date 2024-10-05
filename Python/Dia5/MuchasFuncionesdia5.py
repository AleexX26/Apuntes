"""from random import shuffle

# Lista inicial
palitos = ["-","--","---","----"]

# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# perdirle intentos
def probarSuerte():
    intentos = " "
    
    while intentos not in ["1", "2", "3", "4"]:
        intentos = input("Dime un numero del 1 al 4: ")
    
    return int(intentos)

# comprobar si ha ganado o perdido
def comprobarResultado(lista, intentos):
    if lista[intentos-1] == "----":
        print("Has ganado!")
        return "Ganaste!"
    else:
        print("Has perdido!")
        return "Perdiste!"
    
    print(f"Te ha tocado {lista[intentos-1]}")

# ejecutar la partida
palitosMezclados = mezclar(palitos)
intentos = probarSuerte()
comprobarResultado(palitos, intentos)

"""
import random

def lanzar_dados():
  dado1 = random.randint(1, 6)
  dado2 = random.randint(1, 6)
  return dado1, dado2

def evaluar_jugada(dado1, dado2):
  suma = dado1 + dado2
  if suma <= 6:
    return f"La suma de tus dados es {suma}. Lamentable"
  elif suma < 10:
    return f"La suma de tus dados es {suma}. Tienes buenas chances"
  else:
    return f"La suma de tus dados es {suma}. Parece una jugada ganadora"

# Ejemplo de uso:
resultado_dados = lanzar_dados()
mensaje = evaluar_jugada(*resultado_dados)
print(mensaje)
