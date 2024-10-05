miTuple = (1, 2, 3, 4, 5)
print(type(miTuple))

t = (1, 4.5, "hola", miTuple)
print(type(t))
print(t[0])

miTuple = (1, 2, (10,20), 3)
print(miTuple[2][0])

miTuple = list(miTuple)
print(type(miTuple))

t = (1, 2, 3)

x,y,z = t
print(x, y, z)
