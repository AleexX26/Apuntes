miLista = ['a', 'b', 'c', 'd', 'e']
print(type(miLista))

otraLista = [1, 2, 3, 4, 5, "a", "b", "c", "d", "e"]
print(type(otraLista))

resultado = len(miLista)
print("La lista 'miLista' tiene", resultado, "elementos.")

resultado = miLista[0]
print("El primer elemento de la lista 'miLista' es:", resultado)

resultado = miLista[2:5]
print("Los elementos de la lista 'miLista' entre los índices 2 y 4 son:", resultado)

miLista[0] = "x"
print("El primer elemento de la lista 'miLista' ahora es:", miLista)

miLista.append("f")
print("La lista 'miLista' ahora tiene", len(miLista), "elementos.")
print("La lista 'miLista' ahora tiene", miLista)

miLista.pop(0)
print("La lista 'miLista' ahora tiene", len(miLista), "elementos.")
print("La lista 'miLista' ahora tiene", miLista)

miLista.sort()
print("La lista 'miLista' ahora está ordenada de manera ascendente.", miLista)

miLista.reverse()
print("La lista 'miLista' ahora está ordenada de manera descendente.", miLista)
