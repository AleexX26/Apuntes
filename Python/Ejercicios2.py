print("Pruebas de formato de impresion")
print('--------------------------------\n')

# Inicializamos las variables.
dato1 = 333
dato2 = 202.5
dato3 = "hola"

# Pruebas
print(f'Entero en bases 10, 2 y 16 : {dato1} {dato1:b} {dato1:x}')
print(f'Entero alineado derecha (6 pos rell 0) : {dato1:06}')
print(f'Real sin formato : {dato2}')
print(f'Real con dos decimales : {dato2:.2f}')
print(f'Real alineado derecha (12 pos 0 decim) : {dato2:12.0f}')
print(f'Real alineado derecha (20 pos 2 decim) : {dato2:12.2f}')
print(f'Real con formato exponencial : {dato2:e}')
print(f'Cadena alin. izquierda (20 pos rell =) : {dato3:=<20}')
print(f'Cadena centrada (20 pos rell _) : {dato3:_^20}')
print(f'Cadena alin. derecha (20 pos rell .) : {dato3:.>20}')
