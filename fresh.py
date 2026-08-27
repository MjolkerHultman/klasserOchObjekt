class Tree:
    def __init__(self, height=0,radius=0.0,color=""):
        self.height=height
        self.radius=radius
        self.color=color

    def defineHeight(self, height):
        self.height=height

birch = Tree(9,0.15,"white and black")

input = int(input("define height"))

birch.defineHeight(input)

print(birch.height, birch.radius, birch.color)