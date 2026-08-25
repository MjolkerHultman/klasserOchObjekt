class Person:
    def __init__(self):
        self.förnamn = ''
        self.efternamn = ''
        self.födelseår = ''
        self.singel = True

person1 = Person()
person1.förnamn = "Gremlin"
person1.efternamn = "Mc.Gremlinson"
person1.födelseår = "Tvåtusen åtta"

print(person1.förnamn + person1.födelseår + person1.födelseår)