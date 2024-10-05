nombre = input("Cual es tu nombre: ")
ventas = input("Cuantas ventas realizaste en el mes: ")
comision = 13
ganadoMes = round(float(ventas) * comision, 2)

print(f"El nombre de tu empleado es: {nombre} y ha ganado un total de ${ganadoMes} en comisiones en el mes.")