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


def deal_card():
    import random
    # generates a random suit for the card dealt
    shapeGen = random.randint(1, 4)
    if shapeGen == 1:
        shape = "hearts"
    elif shapeGen == 2:
        shape = "clubs"
    elif shapeGen == 3:
        shape = "spades"
    elif shapeGen == 4:
        shape = "diamond"
    else:
        print("Error in func:dealCard()\nerr:shapeGen issue")
        quit()

    # generates a random number between 1 and 10 for the card's value and assigns it to 'value'
    valueGen = random.randint(1, 10)
    # this IF-statement is unnecessary, but kept incase wanna rework face assignments.
    if valueGen == 1:
        value = 11
    elif valueGen == 10:
        # possibleFaces = ['king', 'queen', 'jack']
        # value = random.choice(possibleFaces)
        value = 10
    elif valueGen < 10 and valueGen > 1:
        value = valueGen
    else:
        print("Error in func:dealCard()\nerr:valueGen issue")
        quit()

    return value, shape


class Player:
    def __init__(self, name, hands={}):
        self.name = name
        self.money = 100
        self.hands = hands
        self.hand_doubled_down = bool
        self.hand_split = bool

    def eval_hand(self, handIndex):
        add = sum(self.hands[handIndex])
        for card in self.hands[handIndex]:
            print(card)
            if card==11:
                if add>21:
                    card=1
                    add = sum(self.hands[handIndex])
                    continue
                break
        return sum(self.hands[handIndex])
       
        # find how many aces in hand
        # find total hand val without aces accounted
        # check if handval is above 21
        # add first ace as 11, check if handval >21
        # if yes, add ace as 1, check if handval >21
        # if handval over 21, bust.
    
    def player_hit(player, handIndex):
        card_value, card_shape = deal_card()
        player.hands[handIndex].append(card_value)
    
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
    player = Player(input('Enter name for Player {}: '.format(i+1)), {0: [11, 11]})
    players.append(player)
print() # spacer to separate roster readback

for player in players:
    print(player.eval_hand(0))

# # player roster readback/check
# for player in players:
#     print("Player {}: {} with ${}".format(players.index(player) + 1, player.name, player.money))

# # still debating what to do with this, will come back to it later
# # readback_verification = lambda verif=input('Is this playerlist correct?[Y/N]: ').upper(): True if verif[0] == 'Y' else False if verif[0] == 'N' else print('invalid input')

# while True:
#     # at start of round, display current stats, clear all hands, and deal new hand
#     print("\n=========================================\nCurrent Stats: ")
#     for player in players:
#         print("{} with ${}".format(player.name, player.money))
#         player.hand_doubled_down = False; player.hand_split = False; player.hands.clear()
#         card_value1, card_shape1 = deal_card()
#         card_value2, card_shape2 = deal_card()
#         player.hands[0] = [card_value1, card_value2]
#     print("=========================================\n")

#     # show each player their hand and ask for play
#     for player in players:
#         print(player.hands[0])
#         print(player.eval_hand(0))

#     # process all playerhands with dealerhand and check for blackjack

#     # too sleepy now, we make later :)

#     # if any player wishes to quit the application between rounds, quit()
#     quitQuery = input("Would any player like to leave the game at this time?[yes/no]: ").upper()
#     if quitQuery[1] == "Y":
#         print('Quitting the application:\nuser executed')
#         break
#     elif quitQuery[1] == "N":
#         continue # break this iteration of while loop and move on to next iteration.
#     else:
#         print("Error in main play loop\nerr:quitQuery not valid")