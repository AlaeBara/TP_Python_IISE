class Animal:
    def faire_du_bruit(self):
        pass
    
class Chien(Animal):
    def faire_du_bruit(self):
        return "Woof! Woof!"

class Chat(Animal):
    def faire_du_bruit(self):
        return "Miaou!"

Chat1 = Chat()
print(Chat1.faire_du_bruit())

Chien1 = Chien()
print(Chien1.faire_du_bruit())