#Comparison method that goes from 6 to 1 in descending order and checks which player is first. Maybe more scalable, therefore somewhat more interesting to muck about with
#nevermind that ^. Make a dict(?) with the saved casts and a name, then sort them by their casts value, then find the name and credit the winning player
#instead just sort the list by cast value and find the last object, that'll be the player that won.
import random
from operator import attrgetter

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.cast = 0

    def throw(self):
        self.cast = random.randrange(1,6)

    def score(self):
        self.score += 1

    def highestCast(self):
        sortedPlayers = sorted(players, key=attrgetter(self.cast))
        return sortedPlayers[-1]


playerCount = int(input("How many players are there?"))
players = []
for i in range(playerCount):
    temporaryObject = Player(input(f"What is the name of player number {str(i + 1)} ?"))
    players.append(temporaryObject)

play = True

while play:
    print("The players rolled...!")
    for i in range(len(players)):
        players[i].throw()
        print(players[i].cast)
    sortedPlayers = sorted(players, key=attrgetter()) #which attribute is this using? I can't reasonably access it like this, outside the class.
    sortedPlayers[-1]
    break

















#for testing the content of players
#for i in range(player_count):
    #print(players[i].name)

#player = Player("HWECFDGWEHFG")
#players = []
    # str("player" + str(i + 1)) = Player()