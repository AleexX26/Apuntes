x = min(56,98,65,3,2,56,)
print(x)
x = min[56,98,65,3,2,56]
print(x)
c = max(56,98,65,3,2,56)
print(c)
c = max [56,98,65,3,2,56]
print(c)

nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis"]
print(min(nombres.lower()))

dic = {"A1": 10, "B2": 20, "C3": 30}
print(min(dic))
print(min(dic.values()))

# Ejercicio 2
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo=max(lista_numeros)
print=valor_maximo

# Ejercicio 3
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

maximo = max(lista_numeros)
minimo = min(lista_numeros)

rango = maximo - minimo

print("El valor máximo es:", maximo)
print("El valor mínimo es:", minimo)
print("La diferencia (rango) entre el máximo y mínimo es:", rango)

# Ejercicio 4
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print("La edad mínima es:", edad_minima)
print("El nombre de la persona es", ultimo_nombre)
