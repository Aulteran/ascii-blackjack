# Primary Dev: Aadil Hussain
# Secondaries: -x-
# Date: March 31, 2023
# Description: This is a blackjack game with multiple players and full economy support.

# Next Goal: transfer playerdata dict methods to python class.

import random

players = {}


def getNum(prompt: str):
    while True:
        try:
            num = int(input(prompt))
            break
        except (ValueError):
            print("Invalid Input, please enter a number.")
    return num


def displayCard(suit, value):
    # depending on suit, makes a nice line on ascii card to fit suit name
    if suit == 'hearts':
        line2 = '|-Hearts-|'
    elif suit == 'clubs':
        pass  # need to finish laterr
    elif suit == 'spades':
        pass  # need to finish laterr
    elif suit == 'diamonds':
        pass  # need to finish laterr
    print("""
----------
|--------| 
    """)  # its 1:30am rn im broken inside, we work on this later lol
    # this is last priority function, can use text identifiers for now. ascii later ig


def Init():
    global players
    # intro
    print("=========================================")
    print("Welcome to the game of Blackjack!")
    print("Each player will be given $100 to begin.")
    print("=========================================")

    # find out how many players will be playing
    numPlayers = getNum("\nHow many players will be playing?: ")

    for num in range(1, numPlayers+1):
        # create playerdata within players dict
        # include name, amount, and hands with hand values within nested dict
        players[num] = {
            "name": input("What is the name for Player %i?: " % num),
            "bank": 100,
            "hands": {1: [0]} #hands is a dict with lists inside because hand 1 will be default. if hand split, additional hands 2 and 3 can be made and 1 un-used.
        }
        print("Okay %s, welcome to the game!\n" % players[num]['name'])
    print("Alright, the players are as follows:")
    for item in players:
        print("Player %i: %s" % (item, players[item]['name']))


def promptOptions(player, canDoubleDown):
    # prompts player to hit or stand
    while True:
        print("%s, what do you want to do?" % player['name'])
        print('''
        Options:
        1. Hit
        2. Stand
        3. Double Down
        4. Back Out of Game''')
        option = getNum("\nEnter your choice: ")
        if option == 1:
            return 'hit'
        elif option == 2:
            return 'stand'
        elif option == 3:
            if canDoubleDown:
                return 'doubdown'
            else:
                print("You can't double down this turn.")
        elif option == 4:
            quit()
        else:
            print("Invalid option, try again.")


canPlayerDoubDown = lambda playerhand: True if playerhand[0] == playerhand[1] else False


def dealCard():
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
        # value = "ace"
        value = 10
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


def playerHit(player, aceCheck):
    raise NotImplementedError


def playerStand(player):
    raise NotImplementedError


def playerDoubleDown(player):
    raise NotImplementedError


def displayHand(hand):
    # func that will count the value of the entire hand, taking into account aces.
    # will also return hand value on top of printing value.
    global aceAvail
    prehandValue = 0
    handValue = 0
    numAces = hand.count(1)
    print('the following cards are of your hand: ', hand)
    
    for card in hand:
        if card != 1:
            prehandValue += card
    
    for i in range(1,numAces+1):
        if prehandValue + 11:
            pass
    
    # discarded
    # hand.sort()
    # 
    # for i in range(hand.index(1), hand.index(1)+numAces):
    #     pass

    print('your hand is valued at ', handValue)

    return handValue


Init()

# loops through, keeping game going until quit executed
while True:
    for player in players:
        # deals player a hand at start of round
        for i in range(0, 2):
            value, shape = dealCard()
            if value == 1:
                aceAvail = True
                pass
            else:
                players[player]['hands'][1].append(value) 
                
        # displays players hand
        hand = displayHand(players[player]['hands'][1])

        # plays the players' hand
        play = promptOptions(player, canPlayerDoubDown(players[player]['hands'][1]))
        if play == 'hit':
            playerHit(player, aceAvail)
        elif play == 'stand':
            playerStand(player)
        elif play == 'doubdown':
            playerDoubleDown(player)
        else:
            print("Error in main play loop\nerr:play not valid")
            quit()

        # clear all player hands after each turn
        for hand in players[player]['hands']:
            players[player]['hands'][hand].clear()

    # if any player wishes to quit the application between rounds, quit()
    quitQuery = input(
        "Would any player like to leave the game at this time?[yes/no]: ").upper()
    if quitQuery[1] == "Y":
        print('Quitting the application:\nuser executed')
        quit()
    elif quitQuery[1] == "N":
        continue # break this iteration of while loop and move on to next iteration.
    else:
        print("Error in main play loop\nerr:quitQuery not valid")
