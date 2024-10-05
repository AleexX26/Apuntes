class padre:
    def hablar(self):
        print("Hola, aprendo del abuelo")


class madre():
    def reir(self):
        print("ja ja")
    
    def hablar(self):
        print("Hola, aprendo de la madre")

class hija(padre, madre):
    pass


class nieto(hija):
    pass

miNieto = nieto()

# miNieto.hablar()
# miNieto.reir()
print(miNieto.__mro__)