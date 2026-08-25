from Bil import Bil

toyota = Bil
toyota.licenseNumber = "ABB 556"
toyota.productionNumber = 45645767
toyota.productionYear = 2020
toyota.weight = 1300
toyota.enginepower = 150

volvo = Bil
volvo.licenseNumber = "ABC 555"
volvo.productionNumber = 100764
volvo.productionYear = 1988
volvo.weight = 1580
volvo.enginepower = 182

from Test import Person

volvo.owner = Person()
volvo.owner.förnamn = "Goober"

print(volvo.owner.förnamn)