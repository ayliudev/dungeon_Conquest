#save
#smooth out battle system 
    #generate random monster
        #read player level
        #scale accordingly
    #battle
        #player chooses action
        #attacks, monster attacks
        #result printed
        #continue battle until life < 0
    #once life < 0
        #You died or
        #You won
            #player experience + 100
    #if level >= #:
        #if player experience >= 200:
            #player level = player level + 1

#skills
#Tutorial (NewGame())
#high score (points for winning battle relative to level)
#turn counter. more points for beating it quickly
#limit on skills (uses?)
#monster uses a random one of 1-4 skills


import random
import time
#checks if there is save data.
try:
    hero = open("/hero.txt")
    Continue()
#no save data, so continues
except:
    NewGame()

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

# hero class, (Simon, Aaron)
class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.health = 100
        self.attack = [5,10]
        self.armour = [5,10]
        self.evasion = [5,10]

        self.str = 0
        self.dex = 0

        self.skills = [Tackle()]

        

# monster class, (Simon, Aaron)
class Monster:
    def __init__(self, name, skills):
        self.name = name
        self.health = 50
        self.attack = [1,10]
        self.armour = [1,10]
        self.evasion = [1,10]
        self.str = 0
        self.dex = 0

        self.skills = [m_Attack()]


#proposal to call menu as an option
def menu():
    print("Menu")
    print("Enter: 1 - New Game, 2 - Continue, 3 - Save, 4 - Character Data, 5 - Save and Quit")

    x = input()
    if x == "1":
        NewGame()
    elif x == "2":
        Continue()
    elif x == "3":
        save()
    elif x == "4":
        info(hero)
    elif x == "5":
        savequit()
    else:
        print("Incorrect input, please enter 1, 2, 3, 4, or 5")
        menu()


#continue menu
def Continue():
    print("Enter: 1 - Battle  2 - Main Menu  3 - Character Information  4 - Save and Quit")
    x = input()
    if x == "1":
        battle()
    elif x == "2":
        menu()
    elif x == "3":
        info()
    elif x == "4":
        savequit()
    else:
        print("Incorrect input, please enter 1, 2, 3, or 4")
        Continue()
def save(hero):

def open_hero():
    hero = open("/hero.txt", "r")
    player = Hero()
    hero = hero.split(",")
    player.name = hero[0]
    player.level = hero[1]
    player.experience = hero[2]
    player.health = hero[3]
    player.attack = hero[4]
    player.armour = hero[5]
    player.evasion = hero[6]

    player.str = [7]
    player.dex = [8]

    player.skills = [9]

    return player

#battle simulation, (Simon, Aaron)
def battle():
    monster_name = ["Ice", "Flame", "Stone"]
    monster_name2 = ["Golem", "Slime", "Wolf"]
    fullname = monster_name[random.randint(0,2)] + monster_name2[random.randint(0,2)]
    player = open_hero()


    #battle takes place
    #if player levels up to 2, 4, 6
        #skills = ["Tackle", "Megaburst"]
        #Choose betwen skills
        #Player chooses tacke
        #player.skills = [tackle()]

    

#prints character info, (Simon, Aaron)
def CharacterData(hero):
    print(hero.name)
    print(f"Health: {hero.health}")
    print(f"Attack: {hero.attack[0]}" + "-" + f"{hero.attack[1]}")
    print(f"Armour: {hero.armour[0]}" + "-" + f"{hero.armour[1]}")
    print(f"Evasion: {hero.evasion[0]}" + "-" + f"{hero.evasion[1]}")

    print(f"Strength: {hero.str}")
    print(f"Dexterity: {hero.dex}")
    print(f"Skills: {hero.skils}")

#tackle()

#Enter: 1 - Attack, 2 - Defend 

def save(player):
    with open('savedata.txt', "w") as f:
        save_slot = player

#Simulates attack, (Simon, Aaron)
def Tackle(player, target):
    #calculates damage
    attack_name = "Tackle"
    damage = random.randint(player.attack[0], player.attack[1]) - random.randint(target.defence[0], target.defence[1])
    #if armour is higher than damage, damage = 0
    if damage < 0:
        damage = 0
    #calculates if enemy dodged
    if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
        print(f"{target.name} dodged the attack!")
    else:
        print(f"{player.name} uses {attack_name} on {target.name}.")
        print(f"{target.name} took {damage} damage!")
        target.health = target.health - damage


#Simulates Monster Attack, (Simon, Aaron)
def m_Attack(enemy, target):
    #calculates damage
    damage = random.randint(enemy.attack[0], enemy.attack[1]) - random.randint(target.defence[0], target.defence[1])
    #if armour is higher than damage, damage = 0
    if damage < 0:
        damage = 0
    #calculates if enemy dodged
    if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
        print(f"You dodged the attack!")
    else:
        print(f"{enemy.name} uses attack on {target.name}.")
        print(f"You took {damage} damage!")
        target.health = target.health - damage


