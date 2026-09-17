#Superklass
class Player():
    def __init__(self,name,level):
        self.name = name
        self.level = level

#Subklass
class Admin(Player):
    def banPlayer(self,targetName):
        print(f"Player {targetName} was banned!")

p1 = Player("Steve", 34)
p2 = Admin("Alex", 345)

p2.banPlayer("Steve")