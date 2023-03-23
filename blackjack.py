players = {}

def getNum(prompt: str):
    while True:
        try:
            num = int(input(prompt))
            break
        except(ValueError):
            print("Invalid Input, please enter a number.")
    return num

def displayCard(face, value):
    if face == 'hearts':
        face = '|-Hearts-|'
    elif face == 'clubs':
        pass
    elif face == 'spacdes':
        pass
    elif face == 'diamonds':
        pass
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

def promptOptions():
    raise NotImplementedError

def dealCard():
    raise NotImplementedError

def playerHit():
    raise NotImplementedError

def playerStand():
    raise NotImplementedError

def doubleDown():
    raise NotImplementedError

Init()