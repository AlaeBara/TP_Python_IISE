class Voiture :
    def __init__(self , marque , modele , annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee
    def afficher_info(self):
        print('{} , {} , {}'.format(self.marque,self.modele,self.annee))



Dacia =Voiture('Dacia' , "StepWay" , 2023)
Dacia.afficher_info()

jetta =Voiture('jetta' , "jetta-0923" , 2022)
jetta.afficher_info()

golf7 =Voiture('golf7' , "golf7-23628" , 2024)
golf7.afficher_info()