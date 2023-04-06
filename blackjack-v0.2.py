'''
Version: 0.2.0
Primary Dev: Aadil Hussain
Secondaries: -x-
Build Date: March 31, 2023
Description: This is a blackjack game with multiple players and full economy support.
Intended Python Version: 3.10.4
Dependancies: random module
'''

import random

def get_int(prompt: str):
    '''gets integer input from user without error'''
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Invalid Input, please enter a whole number.")
    return num


def deal_card():
    '''deals player a random card from deck, joker not included'''

    # generates a random suit for the card dealt
    shape_gen = random.randint(1, 4)
    if shape_gen == 1:
        shape = "hearts"
    elif shape_gen == 2:
        shape = "clubs"
    elif shape_gen == 3:
        shape = "spades"
    elif shape_gen == 4:
        shape = "diamond"
    else:
        print("Error in func:dealCard()\nerr:shape_gen issue")
        quit()

    # generates a random number between 1 and 10 for the card's value and assigns it to 'value'
    value_gen = random.randint(1, 10)
    # this IF-statement is unnecessary, but kept incase wanna rework face assignments.
    if value_gen == 1:
        value = 11
    elif value_gen == 10:
        # possibleFaces = ['king', 'queen', 'jack']
        # value = random.choice(possibleFaces)
        value = 10
    elif value_gen < 10 and value_gen > 1:
        value = value_gen
    else:
        print("Error in func:dealCard()\nerr:value_gen issue")
        quit()

    return value, shape


class Player:
    '''Handles Playerdata as Object'''
    def __init__(self, name, hands={}):
        self.name = name
        self.money = 100
        self.hands = hands
        self.hand_doubled_down = bool
        self.hand_split = bool

    def eval_hand(self, hand_index):
        '''Evaluates value of user's hand'''
        add = sum(self.hands[hand_index])
        loop_iteration = -1
        for card in self.hands[hand_index]:
            loop_iteration += 1
            if card==11:
                if add>21:
                    self.hands[hand_index][loop_iteration] = 1
                    add = sum(self.hands[hand_index])
                    continue
                break
        return sum(self.hands[hand_index])


    def player_hit(self, hand_index):
        '''Deals player another card to current hand'''
        card_value, card_shape = deal_card()
        del card_shape # dumping card_shape to save memory, can recall if decided to use in future.
        player.hands[hand_index].append(card_value)

    def player_stand(self):
        '''Allows player to stand round'''
        raise NotImplementedError

    def player_doubledown(self):
        '''allows player to hit while doubling bet'''
        raise NotImplementedError

    def player_split_hand(self):
        '''splits player hand if hand is splittable'''
        raise NotImplementedError


print("=========================================")
print("Welcome to the game of Blackjack!")
print("Each player will be given $100 to begin.")
print("=========================================")

# how many players
numPlayers = get_int("How many players will be playing?: ")

players = []
# create players
for i in range(numPlayers):
    # Creates player object
    player = Player(input('Enter name for Player {}: '.format(i+1)))
    players.append(player)
print() # spacer to separate roster readback

# player roster readback/check
for player in players:
    print("Player {}: {} with ${}".format(players.index(player) + 1, player.name, player.money))

# still debating what to do with this, will come back to it later
readback_verification = lambda verif=input('Is this playerlist correct?[Y/N]: ').upper(): True if verif[0] == 'Y' else False if verif[0] == 'N' else print('invalid input')

while True:
    # at start of round, display current stats, clear all hands, and deal new hand
    print("\n=========================================\nCurrent Stats: ")
    for player in players:
        print("{} with ${}".format(player.name, player.money))
        player.hand_doubled_down = False; player.hand_split = False; player.hands.clear()
        card_value1, card_shape1 = deal_card()
        card_value2, card_shape2 = deal_card()
        player.hands[0] = [card_value1, card_value2]
    print("=========================================\n")

    # show each player their hand and ask for play
    for player in players:
        print(player.hands[0])
        print(player.eval_hand(0))

    # process all playerhands with dealerhand and check for blackjack

    # too sleepy now, we make later :)

    # if any player wishes to quit the application between rounds, quit()
    quitQuery = input("Would any player like to leave the game at this time?[yes/no]: ").upper()
    if quitQuery[1] == "Y":
        print('Quitting the application:\nuser executed')
        break
    elif quitQuery[1] == "N":
        continue # break this iteration of while loop and move on to next iteration.
    else:
        print("Error in main play loop\nerr:quitQuery not valid")
