def suma(**kwargs):
    print(type(kwargs))
    
suma(x=1, y=2, z=3)

def suma2(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"La clave {clave} tiene el valor {valor}")
        total += valor
    return total

print(suma2(x=1, y=2, z=3))

print("--------------------")
def suma3(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    for arg in args:
        print(f"arg: {arg}")
    for clave, valor in kwargs.items():
        print(f"La clave {clave} tiene el valor {valor}")
    return a + b + sum(args) + sum(kwargs.values())

print(suma3(1, 2, 3, 4, 5, x=6, y=7))

print("--------------------")

def cantidad_atributos(**kwargs):
    total = 0
    for i in kwargs.items():
        print(f"Tiene {total} parametros.")
        total += 1
    return total

print(cantidad_atributos(x=1, y=2, z=3))


print("--------------------")

def lista_atributos(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
    return list(kwargs.values())

# Ejemplo de uso
dict_items = {'color_ojos': 'azules', 'color_pelo': 'rubio'}
resultado = lista_atributos(**dict_items)
print(resultado)  # Salida: ['azules', 'rubio']


print("--------------------")

