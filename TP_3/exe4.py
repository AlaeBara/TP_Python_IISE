class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    # Getters
    def get_nom(self):
        return self.__nom

    def get_prix(self):
        return self.__prix

    
    def calculer_prix_avec_remise(self, remise):
        if self.__prix > 100:
            return self.__prix * (1 - remise)
        return self.__prix



produit = Produit("Ordinateur", 120)
print(f"Prix sans remise: {produit.get_prix()}")  
print(f"Prix avec remise de 10%: {produit.calculer_prix_avec_remise(0.10)}")
