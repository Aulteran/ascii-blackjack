# Version: 0.2.0
# Primary Dev: Aadil Hussain
# Secondaries: -x-
# Date: March 31, 2023
# Description: This is a blackjack game with multiple players and full economy support.


def getNum(prompt: str):
    while True:
        try:
            num = int(input(prompt))
            break
        except (ValueError):
            print("Invalid Input, please enter a whole number.")
    return num


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.hands = {}
        self.hand_doubled_down = bool
        self.hand_split = bool
    
    def player_hit():
        raise NotImplementedError
    
    def player_stand():
        raise NotImplementedError
    
    def player_doubledown():
        raise NotImplementedError
    
    def player_split_hand():
        raise NotImplementedError
    

print("=========================================")
print("Welcome to the game of Blackjack!")
print("Each player will be given $100 to begin.")
print("=========================================")

# how many players
numPlayers = getNum("How many players will be playing?: ")

players = []
# create players
for i in range(numPlayers):
    # Creates player object
    player = Player(input('Enter name for Player {}: '.format(i+1)))
    players.append(player)

# player roster readback/check
for player in players:
    print("Player {}: {} with ${}".format(players.index(player) + 1, player.name, player.money))

