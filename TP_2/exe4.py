class Persone:
    def __init__(self, nom , prenom, age):
        self.nom = nom 
        self.prenom= prenom
        self.age=age
    def se_presenter(self):
        print("{} ,{}, {}".format(self.nom , self.prenom , self.age))
    

class Etudiant(Persone):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule

    def etudier(self):
        print(f"L'étudiant {self.prenom} {self.nom} (matricule : {self.matricule}) est en train d'étudier.")


person = Persone("Dupont", "Jean", 35)
person.se_presenter()

etudiant = Etudiant("Martin", "Alice", 20, "123456")
etudiant.se_presenter()
etudiant.etudier()