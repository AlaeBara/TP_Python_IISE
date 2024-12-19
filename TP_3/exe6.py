class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    # Getters
    def get_nom(self):
        return self.__nom

    def get_prix(self):
        return self.__prix

    # Méthode pour calculer le prix avec remise
    def calculer_prix_avec_remise(self, remise):
        if self.__prix > 100:
            return self.__prix * (1 - remise)
        return self.__prix


class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def total_commande(self):
        return self.produit.get_prix() * self.quantite

class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def total_panier(self):
        total = 0
        for commande in self.commandes:
            total += commande.total_commande()
        return total


produit1 = Produit("Livre", 20)
produit2 = Produit("T-shirt", 15)

commande1 = Commande(produit1, 2)  
commande2 = Commande(produit2, 3) 

panier = Panier()
panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)

print(f"Total du panier: {panier.total_panier()}") 
