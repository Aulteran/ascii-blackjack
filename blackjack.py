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
        break #need to finish laterr
    elif suit == 'spacdes':
        break #need to finish laterr
    elif suit == 'diamonds':
        break #need to finish laterr
    print("""
----------
|--------| 
    """) # its 1:30am rn im broken inside, we work on this later lol

def Init():
    global players
    # intro
    print("=========================================")
    print("Welcome to the game of Blackjack!")
    print("Each player will be given $1000 to begin.")
    print("=========================================")

    # find out how many players will be playing
    numPlayers = getNum("\nHow many players will be playing?: ")
    
    for num in range(1, numPlayers+1):
        players[num] = {
            "name": input("What is the name for Player %i?: "%num),
            "bank": 1000
        }
        print("Okay %s, welcome to the game!\n"%players[num]['name'])
    print("Alright, the players are as follows:")
    for item in players:
        print("Player %i: %s"%(item, players[item]['name']))

def promptOptions(player):
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
            break
        elif option == 2:
            break
        elif option == 3:
            break
        elif option == 4:
            quit()
        else:
            print("Invalid option, try again.")
    raise NotImplementedError

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
        print("Error in func:dealCard()")
        quit()

    #generates a random number between 1 and 13 for the card's value and assigns it to 'value'
    valueGen = random.randint(1,13)
    if valueGen == 1:
        value = "ace"
    else: #could make this more robust by being specific instead of else statement, use else for error+quit
        value = str(valueGen)

def playerHit(player):
    raise NotImplementedError

def playerStand(player):
    raise NotImplementedError

def doubleDown(player):
    raise NotImplementedError

Init()