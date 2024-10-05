def palabraAdivinar(palabra):
    # Crear una cadena de guiones bajos con la misma longitud que la palabra
    return "_" * len(palabra)

def comprobarLetra(palabra_adivinar, letra, palabra):
    # Si la letra está en la palabra original, actualizar la representación oculta
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_adivinar = palabra_adivinar[:i] + letra + palabra_adivinar[i + 1:]
    return palabra_adivinar

def jugar():
    # Definimos la palabra
    palabra = "hola"
    palabra_oculta = palabraAdivinar(palabra)
    
    intentos = 6  # Número de intentos permitidos

    print("¡Bienvenido al juego de adivinar la palabra!")
    print("La palabra a adivinar es:", palabra_oculta)

    while intentos > 0 and "_" in palabra_oculta:
        letra = input("Adivina una letra: ").lower()
        
        # Comprobar si la letra ya fue adivinada
        if letra in palabra_oculta:
            print("Ya has adivinado esa letra. Intenta otra vez.")
            continue
        
        # Comprobar y actualizar la palabra oculta
        palabra_oculta = comprobarLetra(palabra_oculta, letra, palabra)
        
        if letra not in palabra:
            intentos -= 1
            print(f"La letra '{letra}' no está en la palabra. Te quedan {intentos} intentos.")
        
        print("Palabra actual:", palabra_oculta)

    if "_" not in palabra_oculta:
        print("¡Felicidades! Has adivinado la palabra:", palabra)
    else:
        print("¡Se han acabado los intentos! La palabra era:", palabra)

# Iniciar el juego
jugar()
