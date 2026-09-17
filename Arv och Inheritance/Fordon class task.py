class Fordon():
    def __init__(self,maxSpeed,regNr):
        self.maxSpeed = maxSpeed
        self.regNr = regNr

class Car(Fordon):
    def __init__(self, maxSpeed, regNr, example):
        super().__init__(maxSpeed, regNr)
        self.example = example

    def proposition():
        print("example text car")

class suppose(Fordon):
    def __init__(self, maxSpeed, regNr):
        super().__init__(maxSpeed, regNr)