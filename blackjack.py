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
        players[num] = {
            "name": input("What is the name for Player %i?: "%num),
            "bank": 100
        }
        print("Okay %s, welcome to the game!\n"%players[num]['name'])
    print("Alright, the players are as follows:")
    for item in players:
        print("Player %i: %s"%(item, players[item]['name']))

# unsure if i need this func
# def promptOptions():
#     raise NotImplementedError

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
    elif valueGen < 1 and valueGen > 10:
        value = str(valueGen)
    else:
        print("Error in func:dealCard()\nerr:valueGen issue")
        quit()

def playerHit(player):
    raise NotImplementedError

def playerStand(player):
    raise NotImplementedError

def doubleDown(player):
    raise NotImplementedError

Init()