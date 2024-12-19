from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        return 3.14 * self.rayon ** 2

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur


cercle = Cercle(5)
rectangle = Rectangle(4, 6)

print(f"Surface du cercle: {cercle.calculer_surface()}")  
print(f"Surface du rectangle: {rectangle.calculer_surface()}") 
