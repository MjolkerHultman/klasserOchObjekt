#Comparison method that goes from 6 to 1 in descending order and checks which player is first. Maybe more scalable, therefore somewhat more interesting to muck about with
#nevermind that ^. Make a dict(?) with the saved casts and a name, then sort them by their casts value, then find the name and credit the winning player
import random

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.cast = 0

    def throw(self):
        self.cast = random.randrange(1,6)

    def score(self):
        self.score += 1

playerCount = int(input("How many players are there?"))
players = []
for i in range(playerCount):
    temporaryObject = Player(input(f"What is the name of player number {str(i + 1)} ?"))
    players.append(temporaryObject)

play = True

while play:
    for player in players:

















#for testing the content of players
#for i in range(player_count):
    #print(players[i].name)

#player = Player("HWECFDGWEHFG")
#players = []
    # str("player" + str(i + 1)) = Player()