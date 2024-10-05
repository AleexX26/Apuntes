import random

def generar_tarjeta_bingo():
    tarjeta = []
    
    # Generar números por columna (rangos específicos para cada columna)
    rangos_columnas = {
        'B': range(1, 16),
        'I': range(16, 31),
        'N': range(31, 46),
        'G': range(46, 61),
        'O': range(61, 76),
    }
    
    for letra in ['B', 'I', 'N', 'G', 'O']:
        # Elegir 5 números aleatorios de cada rango (4 en la columna 'N' por el espacio libre)
        if letra == 'N':
            columna = random.sample(rangos_columnas[letra], 4)
            columna.insert(2, "LIBRE")  # El espacio central es "LIBRE"
        else:
            columna = random.sample(rangos_columnas[letra], 5)
        tarjeta.append(columna)
    
    # Transponer la matriz para mostrarla en formato de tarjeta
    tarjeta_transpuesta = list(map(list, zip(*tarjeta)))  # Pasamos las columnas a filas
    return tarjeta_transpuesta

# Generamos una tarjeta de bingo de ejemplo
tarjeta_bingo = generar_tarjeta_bingo()
for fila in tarjeta_bingo:
    print(fila)
