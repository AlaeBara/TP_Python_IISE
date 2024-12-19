from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass

class Voiture(Vehicule):
    def deplacer(self):
        return "La voiture roule sur la route."

class Bicyclette(Vehicule):
    def deplacer(self):
        return "La bicyclette roule sur un chemin."


voiture = Voiture()
bicyclette = Bicyclette()

print(voiture.deplacer())  
print(bicyclette.deplacer())  


#name mangling => print(P._Persone__nome) in cas de variable priver meme si ila priver.
