class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print("El animal ha nacido")

class Pajaro(Animal):
    pass

piolin = Pajaro(2, "amarillo")
# piolin.nacer()
print(piolin.color)

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

class Mascota():
    def __init__(self, edad, nombre, cantidad_patas):
        self.nombre = nombre
        self.edad = edad
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass


class Vehiculo:
    def acelerar(self):
        pass

    def frenar(self):
        pass

class Automovil(Vehiculo):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

mi_auto = Automovil("Toyota", "Corolla")
print(f"Marca: {mi_auto.marca}, Modelo: {mi_auto.modelo}")

mi_auto.acelerar()
mi_auto.frenar()
