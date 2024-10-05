palabras = "python"
lista = []
for letra in palabras:
    lista.append(letra)
print(lista)


palabras = "python"
lista = [letra for letra in palabras]
print(lista)

lista =[n for n in range(1, 11, 1)]
print(lista)

lista = [n for n in range(1, 11) if n % 2 == 0]
print(lista)

lista = [ n if n % 2 == 0 else "no" for n in range(1, 11)]
print(lista)

pies = [10,20,30,40,50]
metros = [p / 3.281 for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [c ** 2 for c in valores]

valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = []
for p in valores:
    if p % 2 ==0:
        valores_pares.append(p)
        
temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(f - 32) * (5/9) for f in temperatura_fahrenheit]

print(grados_celsius)