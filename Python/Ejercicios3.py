
# Asignación:
print("variable = expresión")
# Por ejemplo:
x = 4
x = y = 0
x , y = 4 , 5
x , y = [4 , 5]
z = x - y
a = 'hola'
b = 'ase'
c = a + ' k ' + b
d = '-' * 10
e = ("El resultado es:",  x, z, a, b, c, d)
print (str(e))  

# Operadores:
# - aritméticos: + , - , * , / , // , % , **
# - lógicos: < , <= , > , >= , == , != , and , or , not

# Funciones matemáticas:
#  math.abs() , math.sin() , math.log() , math.sqrt() , math.pi, etc.
# Pero hay que escribir a inicio del programa, como primera línea:
#  import 

# Conversión entre tipos de datos:
# - a entero (tipo de datos “int”): int('25') , int(25.9) , round(25.9)

# - a real (tipo de datos “float”): float('25.5') , float(25)
# - a cadena (tipo de datos “string”): str(25.5)

# Entrada por teclado:
#  variable = input('texto a imprimir')
# Por ejemplo:
#  nombre = input('¿Cómo te llamas? ')
#  edad = int( input('¿Cuántos años tienes? ') )
#  r = float( input('¿Qué mide el radio? ') )

# Entrada por línea de comandos (como argumentos del programa):
#  from sys import argv
#  print('El nombre del programa es', argv[0])
#  print('El primer argumento es', argv[1])
#  print('El segundo argumento es', argv[2])

# Salida por consola:
#  print('text a imprimir', variables, ...)
# Por ejemplo:
#  print('Hola', nombre)
#  print(a, b, c, sep='|', end=' ')
#  print('resultado','\t',3*5,'\n')
#  print('''
#  Este texto
#  ocupa varias líneas
#  ''')
#  print('El nombre es %s y la edad %d años' % (nombre, edad))
#  print(f'El nombre es {nombre} y la edad {edad} años')
#  print(f'Área: {(PI*r*r):7.2f}')