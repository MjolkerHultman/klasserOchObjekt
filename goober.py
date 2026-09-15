class Person:
    def __init__(self,namn, ålder):
        self.namn = namn
        self.__ålder = ålder

    def getÅlder(self):
        return self.__ålder

    def setÅlder(self, nyÅlder):
        self.__ålder = nyÅlder

person = Person("Anna",25)
person.setÅlder(29)

print(person.namn)
print(person.getÅlder())

# print(person.__ålder) "__" makes stuff private.