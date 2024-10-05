def verificar_ceros_consecutivos(*args):
    # Iteramos sobre los argumentos
    for i in range(len(args) - 1):
        # Comparamos el elemento actual con el siguiente
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

# Ejemplo de uso
resultado1 = verificar_ceros_consecutivos(1, 2, 0, 0, 4)
resultado2 = verificar_ceros_consecutivos(1, 0, 2, 0, 4)

print(resultado1)  # Salida: True
print(resultado2)  # Salida: False
