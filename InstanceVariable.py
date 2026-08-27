class Cirkel:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 0

cirkel = Cirkel()

cirkel.x = 100
cirkel.y = 24355
cirkel.r = 12423

#Alternatively...

class BättreCirkel:
    def __init__(self, x=0,y=0,r=0):
        self.x = x
        self.y = y
        self.r = r

superiorCircle = BättreCirkel(23,345,124)

print(superiorCircle)