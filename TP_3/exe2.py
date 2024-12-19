class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    # Getters
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_age(self):
        return self.__age

    # Setters
    def set_nom(self, nom):
        self.__nom = nom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("L'âge doit être un nombre positif.")


personne = Personne("Dupont", "Pierre", 30)
print(personne.get_nom())  
print(personne._Personne__nom)  
print(personne.get_prenom()) 
print(personne.get_age()) 

personne.set_age(35)
print(personne.get_age())  


personne.set_age(-5)  
