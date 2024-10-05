def letras_unicas_en_orden(palabra):
    caracteres_unicos = set(palabra.lower())
    lista_ordenada = sorted(caracteres_unicos)
    return lista_ordenada

resultado = letras_unicas_en_orden("entretenido")
print(resultado)

