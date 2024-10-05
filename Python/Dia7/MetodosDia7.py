class Pajaro:
    
    alas = True
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    
    def piar(self):
        print("Pio, mi color es {}".format(self.color))
    
    
    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")
        
piolin = Pajaro("amarillo", "canario")
piolin.piar()
piolin.volar(100)


class Perro:
    
    def ladrar(self):
        print("Guau, guau!")

perro = Perro()

class Mago:
    
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()

class Alarma:
    def cantidad_minutos(self, minutos):
        print("La alarma ha sido pospuesta {cantidad_minutos} minutos")

alarma = Alarma()
alarma.cantidad_minutos(5)