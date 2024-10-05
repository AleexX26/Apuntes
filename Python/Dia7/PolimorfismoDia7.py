class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"{self.nombre} está gritando: mmmm, mmmm, mmmm!")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"{self.nombre} está gritando: quuuu, quuuu, quuuu!")

vaca1 = Vaca("Pablo")
oveja1 = Oveja("Marta")

# print(vaca1.nombre)
# print(oveja1.nombre)

# animales = [vaca1, oveja1]
# for animal in animales:
#     animal.hablar()

# def animalHabla(animal):
#     animal.hablar()

# animalHabla(vaca1)
# animalHabla(oveja1)