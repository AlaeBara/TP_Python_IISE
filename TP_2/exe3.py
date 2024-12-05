class CompteBancaire:
    def __init__(self , titulaire, sold):
        self.titulaire=titulaire
        self.sold=sold
    def desposer(self,montant):
        self.sold +=montant
    def retirer(self,montant):
        self.sold -=montant
    def affiche_sold(self):
        print(' votre sold est : {}'.format(self.sold))



C1=CompteBancaire('BMCE' , 100)

C1.desposer(1000)

C1.affiche_sold()

C1.retirer(150)

C1.affiche_sold()

