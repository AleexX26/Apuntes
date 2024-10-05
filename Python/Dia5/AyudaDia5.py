dic = {"Clave1": 100, "Clave2": 200, "Clave3": 300}

a = dic.popitem()
print(a)
print(dic)

#Ejercicio 2
# Definir la cadena original
cadena = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

# Aplicar lstrip para eliminar los caracteres especificados
resultado = cadena.lstrip(",:%_#")

# Imprimir el resultado
print(resultado)


#Ejercicio 3
# Definir la lista original
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

# Insertar "naranja" en la cuarta posición (índice 3)
frutas.insert(3, "naranja")

# Imprimir la lista modificada
print(frutas)


#Ejercicio 4
# Definir los conjuntos
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

# Verificar si los conjuntos son aislados
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

# Imprimir el resultado
print(conjuntos_aislados)

