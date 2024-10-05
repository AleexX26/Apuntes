class Pajaro:
    
    alas = True
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    
    def piar(self):
        print("Pio, mi color es {}".format(self.color))
    
    
    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")
        self.piar()
    
    
    def pintar_negro(self):
        self.color = "negro"
        print("El pajaro ahora es {}".format(self.color))
    
    @classmethod
    def ponerHuevos(cls, cantidad):
        print(f"Se ponen {cantidad} huevos en la nido")
        cls.alas = False
        print(f"El pajaro ahora tiene alas: {cls.alas}" )

Pajaro.ponerHuevos(5)


    @staticmethod
    def mirar():
        print("Estoy mirando")


# piolin = Pajaro("amarillo", "canario")
# piolin.volar(50)
# piolin.alas = False
# print(piolin.alas)

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True

print(Jugador.vivo)
Jugador.revivir()
print(Jugador.vivo)
