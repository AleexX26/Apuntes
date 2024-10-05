class Pajaro:
    
    alas = True
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        

miPajaro = Pajaro("rojo", "Africano")
print(f"mi pajaro es de color {miPajaro.color} y especie {miPajaro.especie}  ")

print(Pajaro.alas)
print(miPajaro.alas)


class Cubo:
    caras = 6
    
    def __init__(self, color):
        self.color = color
        
cubo_rojo = Cubo("rojo")

print(Cubo.caras)
print(cubo_rojo.color)


class Personaje:
    
    real = False
    
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje("Humano", "True", "17")

print(harry_potter)
