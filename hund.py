class Rectangle():
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def calcArea(self):
        return self.width * self.height
    def setHeight(self, height):
        self.height = height

marbleTabletop = Rectangle(0.2, 5)

marbleTabletop.setHeight(34)
print(marbleTabletop.calcArea())