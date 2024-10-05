nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis"]
edades = [25, 30, 28, 22, 27]
ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Murcia"]

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

#Ejercicio 2
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinado = list(zip(capitales, paises))
for capitales, paises in combinado:
    print(f"La capital de {paises} es {capitales}")

#Ejercicio 3
marcas = ["Apple", "Samsung", "Huawei", "Xiaomi", "Oppo"]
productos =["iPhone", "Smartphone", "Móvil", "Tablet", "Smartwatch"]
mi_zip = list(zip(marcas, productos))

for marcas, productos in mi_zip:
    print(f"La marca {marcas} tiene como producto {productos}")

#Ejercicio 4
espanol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espanol, portugues, ingles))

print(numeros)