miLista = [1, 2, 3, 4, 5]
print(miLista)

class Objeto:
    pass

miObjeto = Objeto()
print(miObjeto)

class CD:
    def __init__(self, autor,titular, canciones):
        self.titular = titular
        self.canciones = canciones
        self.autor = autor
    
    def __str__(self):
        return f"CD: {self.titular}, Autor: {self.autor}, Canciones: {self.canciones}"
    
    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print("Se ha eliminado el CD")


miCD = CD("Beatles", "Abbey Road", 34)
print(len(miCD))

# del miCD
# print(miCD)