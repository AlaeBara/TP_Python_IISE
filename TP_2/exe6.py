class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)

rect = Rectangle(5, 10)
print("Surface:", rect.calculer_surface())
print("Périmètre:", rect.calculer_perimetre())
