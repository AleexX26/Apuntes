class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print("El animal ha nacido")
        
    def hablar(self):
        print("El animal está hablando")

class Pajaro(Animal):
    
    def __init__(self, edad, color, altura):
        super().__init__(edad, color)
        self.altura = altura
    
    
    def hablar(self):
        print("pio")
    
    def volar(self, metros):
        print(f"El pajaro está volando {metros} metros")



piolin = Pajaro(2, "amarillo", 60)
miAnimal = Animal(3, "rojo"  )

miAnimal.hablar()

piolin.nacer()

piolin.hablar()

piolin.volar(100)
