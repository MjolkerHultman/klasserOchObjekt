class Person:
    def __init__(self):
        self.förnamn = ""
        self.efternamn = ""

class Hus:
    def __init__(self):
        self.hustyp = ""
        self.ägare = None

hus = Hus()
hus.hustyp = "Villa"

jesper = Person()
jesper.förnamn = "Jesper"
hus.ägare = jesper

