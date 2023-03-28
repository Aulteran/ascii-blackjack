import random

players = {}

def getNum(prompt: str):
    while True:
        try:
            num = int(input(prompt))
            break
        except(ValueError):
            print("Invalid Input, please enter a number.")
    return num

def displayCard(suit, value):
    #depending on suit, makes a nice line on ascii card to fit suit name
    if suit == 'hearts':
        line2 = '|-Hearts-|'
    elif suit == 'clubs':
        pass #need to finish laterr
    elif suit == 'spades':
        pass #need to finish laterr
    elif suit == 'diamonds':
        pass #need to finish laterr
    print("""
----------
|--------| 
    """) # its 1:30am rn im broken inside, we work on this later lol
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
            "name": input("What is the name for Player %i?: "%num),
            "bank": 100,
            "hands": {1:[]}
        }
        print("Okay %s, welcome to the game!\n"%players[num]['name'])
    print("Alright, the players are as follows:")
    for item in players:
        print("Player %i: %s"%(item, players[item]['name']))

def promptOptions(player, canDoubleDown):
    # prompts player to hit or stand
    while True:
        print("%s, what do you want to do?"%player['name'])
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

def canPlayerDoubDown(playerhand):
    if playerhand[1] == playerhand[2]:
        return True
    else:
        return False

def dealCard():
    #generates a random suit for the card dealt
    shapeGen = random.randint(1,4)
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

    #generates a random number between 1 and 13 for the card's value and assigns it to 'value'
    valueGen = random.randint(1,10)
    if valueGen == 1:
        value = "ace"
    elif valueGen == 10:
        possibleFaces = ['king', 'queen', 'jack']
        value = random.choice(possibleFaces)
    elif valueGen < 10 and valueGen > 1:
        value = str(valueGen)
    else:
        print("Error in func:dealCard()\nerr:valueGen issue")
        quit()
    
    return value, shape

def playerHit(player):
    raise NotImplementedError

def playerStand(player):
    raise NotImplementedError

def playerDoubleDown(player):
    raise NotImplementedError

Init()

# initial dealt hand:
# to be coded
while True:
    for player in players:
        # deals player a hand at start of round
        value, shape = dealCard()
        players[player]['hands'][1] += value

        # plays the players' hand
        play = promptOptions(player, canPlayerDoubDown(players[player]['hand']))
        if play == 'hit':
            playerHit(player)
        elif play == 'stand':
            playerStand(player)
        elif play == 'doubdown':
            playerDoubleDown(player)
        else:
            print("Error in main play loop\nerr:play not valid")

    # if any player wishes to quit the application between rounds, quit()
    quitQuery = input("Would any player like to leave the game at this time?[yes/no]: ").upper()
    if quitQuery[1] == "Y":
        quit()
    elif quitQuery[1] == "N":
        continue
    else:
        print("Error in main play loop\nerr:quitQuery not valid")