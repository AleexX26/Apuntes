import os

ruta = os.getcwd()

ruta = os.chdir("G:\\Mi unidad\\2Dam\\Programacion\\Alex\\CurosPy")

crearCarpeta = os.mkdir("CarpetaPrueba")
print(f"Carpeta creada correctamente: {crearCarpeta}")

elemento = os.path.basename(ruta)
elemento = os.path.dirname(ruta)
elemento = os.path.split(ruta)

os.rmdir("CarpetaPrueba")
print(f"Carpeta eliminada correctamente: {os.path.exists('CarpetaPrueba')}")

print(f"La ruta actual es: {ruta}")


otroArchivo = open("G:º\Mi unidad\\2Dam\\Programacion\\\CurosPy\\Dia6\\Prueba.txt")

print(f"El nombre del archivo es: {otroArchivo.name}")



from pathlib import Path


miPath = Path("G:\\Mi unidad\\2Dam\\Programacion\\Alex\\CurosPy\\Dia6")
archivo = carpeta / "Prueba.txt"

minArchivo = open(archivo)

print(f"El nombre del archivo es: {minArchivo.name}")