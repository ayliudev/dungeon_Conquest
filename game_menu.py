import random
import time
#checks if there is save data.

if __name__ == '__main__':
    print("Welcome to ___")
    try:
        hero = open("/hero.txt")
        Continue()
    #no save data, so continues
    except:
        NewGame()
    while game = True:
        print("Menu")
        print("Enter options '1 - 5':")
        print("1 - New Game")
        print("2 - Continue")
        print("3 - Save")
        print("4 - Character Data")
        print("5 - Save and Quit")
        

        if option == 5:
            # Save and quit
            game = False
            




    

def NewGame():
    print("Welcome to ____")
    print("Please enter your Character name")
    x = str(input())
    player = Hero(x)
    print(f"Welcome {hero.name}")
    #Below here are the instructions to the game
    print("")
    save(player)
    Continue()
