from pathlib import Path, PureWindowsPath

carpeta = Path("G:\\Mi unidad\\2Dam\\Programacion\\Alex\\CurosPy\\Dia6\\Prueba.txt")

rutaWindows = PureWindowsPath(carpeta)

print(rutaWindows)

print(carpeta.name )
print(carpeta.suffix)
print(carpeta.stem)
print(carpeta.read_text())

if not carpeta.exists():
    print("El archivo no existe")
else:
    print("El archivo existe")


