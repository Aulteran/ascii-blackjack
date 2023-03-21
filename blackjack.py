players = {}

def getNum(prompt: str):
    while True:
        try:
            num = int(input(prompt))
            break
        except(ValueError):
            print("Invalid Input, please enter a number.")
    return num

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
        print("Okay %s, welcome to the game!"%(players[num])['name'])
    print("Alright, the players are as follows:")
    # i rlly dont feel like finishing this rn

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