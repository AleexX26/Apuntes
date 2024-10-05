# def miFuncion():
#     return 4

# def miLista():
#     lista = []
#     for x in range(1,5):
#         lista.append(x*10)
#     return lista

# def miGenerador2():
#     for x in range(1,5):
#         yield x*10


# print(miGenerador2())
# h = miGenerador2()
# print(next(h))
# print(next(h))
# print(next(h))


# def miGenerador():
#     yield 4,5

# print(miFuncion())
# print(miGenerador())

# g = miGenerador()
# print(next(g))



def miGenerador():
    x = 1
    yield x
    
    x += 1
    yield x
    
    x += 1
    yield x

g = miGenerador()
print(next(g))
print(next(g))

print("Hola mundo")


print(next(g))
