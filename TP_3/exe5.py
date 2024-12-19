class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.employes = []

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def afficher_employes(self):
        for employe in self.employes:
            print(f"{employe.nom} {employe.prenom}")



manager = Manager("Martin", "Jacques", 5000)
employe1 = Employe("Lemoine", "Paul", 3000)
employe2 = Employe("Durand", "Marc", 3200)

manager.ajouter_employe(employe1)
manager.ajouter_employe(employe2)

manager.afficher_employes()
