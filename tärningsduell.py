#Comparison method that goes from 6 to 1 in descending order and checks which player is first. Maybe more scalable, therefore somewhat more interesting to muck about with

from random import random

class Player():
    def __init__(self, name, ):
        self.name = name
        self.score = 0

player_count = int(input("How many players are there?"))
players = []
for i in range(player_count):
    temporaryObject = Player(input("What is the name of player number " + str(i + 1) + "?"))
    players.append(temporaryObject)

for i in range(player_count):
    print(players[i].name)

#player = Player("HWECFDGWEHFG")
#players = []
    # str("player" + str(i + 1)) = Player()