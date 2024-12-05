class Chien:
    def __init__(self,nom , race , age):
        self.nom = nom 
        self.race = race
        self.age=age
    
    def aboyer(self):
        print('Woof!')


S1=Chien("aza","chien",12)
S1.aboyer()


