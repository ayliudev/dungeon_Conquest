
#Tutorial (NewGame())


#Refresh Screen and a visual bar for health



#Completed ---
#better interface
#Time
#high score
#skills
#Balance monsters and skills
#limit on skills (uses?)
#monster uses a random one of 1-4 skills
#Research
    #exception for capturing key presses
#save(Finished)
#smooth out battle system 
    #read player level
        #if player reaches level 5
            #option appears to fight mid-boss
        #if player reaches level 10
            #option appears to fight final boss fight
        #generate random monster
            #scale monster stats by level, (2, 4, 6, 8)
    #battle
        #player chooses action
        #player attacks, monster attacks
        #result printed
        #continue battle until life < 0
        
        #once life < 0
            #You died or
            #You won
                #player experience + 10
                #you gained 10 experience
        #if player experience >= 30:
                #player level = player level + 1
                #print(you leveld up, choose 1 for 1 point in str or 2 for 1 point in dex)
                #str(msvcrt.getch()).strip("b").strip("'")
                #You can choose one new skill
                    #pickbetween one or two
                #
            #save player data in to text file
#Completed ---


import random
import time
import json
import sys
import msvcrt
import os


def NewGame():
    print("#############################")
    print("Welcome to Dungeon Conquest")
    print("#############################")
    print(" ")
    time.sleep(1)
    print("Please enter your Character name")
    x = input()
    player = Hero()
    player.name = x
    os.system("cls")
    print(f"Welcome {player.name}!")
    time.sleep(1)
    #Below here are the instructions to the game
    print("")
    midboss()
    finalboss()
    save(player)

# hero class, (Simon, Aaron)
class Hero:
    def __init__(self):
        self.name = "initial"
        self.level = 1
        self.experience = 0
        self.highscore = 0
        self.turns = 0
        self.str = 0
        self.dex = 0

        self.health = 100 + (50*self.str) + (50*self.dex)
        self.attack = [(5 + (5*self.str) + (5*self.dex)),(10 + (5*self.str) + (5*self.dex))]
        self.armour = [(1 + (5*self.str)), (10 + (5*self.str))]
        self.evasion = [(1 + (5*self.dex)), (10 + (5*self.dex))]
        self.skills = ["Attack"]
        self.sp = 40 + (10*self.dex)
        self.all_skills = ["Attack", "Thrust", "Armour_Breaker", "Tendon_Cut", "Berserker_Slash", "Sacrifice",
                           "Sexy_Wink", "Glob_of_Glue", "Armour_Up","Evasive_Boost", "Heal" ]
    
    def __eq__(self, target):
        if self.name == target.name:
            return True
        else:
            return False
# the following class methods will be used as skills, it is clumsy, but difficult to make interesting skills otherwise
##### skill start #####################################################

    def Attack(self, target):
        
    #calculates damage
        attack_name = "Attack"
        damage = random.randint(self.attack[0], self.attack[1]) - random.randint(target.armour[0], target.armour[1])
    #if armour is higher than damage, damage = 0
        if damage < 0:
            damage = 0
    #calculates if enemy dodged
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} took {damage} damage!")
            target.health = target.health - 1000000000

    def Thrust(self,target):  # Same as attack, but ignores some of the target's armour
        attack_name = "Thrust"
        damage = random.randint(self.attack[0], self.attack[1]) - random.randint(target.armour[0], target.armour[1] -2)
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            
            
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name}'s armour was pierced for {damage} damage!")
            target.health = target.health - damage
        self.sp = self.sp - 5

    def Armour_Breaker(self,target):  # Is weaker than attack, but damages target's armour
        attack_name = "Armour Breaker"
        damage = random.randint(round(self.attack[0]), round(self.attack[1]/1.999)) - random.randint(target.armour[0], target.armour[1])
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name}'s armour was thrashed for {damage} damage!")
            target.health = target.health - damage
            if target.armour[1] > target.armour[0]:  # Insures that max armour does not go below minimum
                target.armour[1] = target.armour[1] - (round(self.attack[1]/2+0.1))
                if target.armour[1] < target.armour[0]:
                    target.armour[1] = target.armour[0]
            self.sp = self.sp - 15

    def Tendon_Cut(self,target):  # Weaker than attack, but damages target's evasion
        attack_name = "Tendon Cut"
        damage = random.randint(self.attack[0], round(self.attack[1]/1.999)) - random.randint(target.armour[0], target.armour[1])
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name}'s tendons were cut for {damage} damage!")
            target.health = target.health - damage
            if  target.evasion[1] >  target.evasion[0]:
                target.evasion[1] = round(target.evasion[1] * 0.80)
        self.sp -= 10

    def Berserker_Slash(self,target):  # Does 3 times the damage of attack, but damages hero in the process
        attack_name = "Beserker Slash"
        damage = random.randint(self.attack[0]*3, self.attack[1]*3) - random.randint(target.armour[0], target.armour[1])
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} was brutally slashed for {damage} damage, but {self.name} was hurt by the attack!")
            self.health -= (self.health * 0.25)
            target.health = target.health - damage
            self.sp -= 20

    def Sacrifice(self,target): # Does 10 times the damage of attack, but uses half of hero health
        attack_name = "Sacrifice"
        damage = random.randint(self.attack[0]*10, self.attack[1]*10) - random.randint(target.armour[0], target.armour[1])
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(60,100):
            
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"""{self.name} knows the true meaning of sacrifice"
                  \n{target.name} took {damage} damage in an all out attack, but {self.name} was severly hurt by the attack!""")
            self.health -= (self.health * 0.5)
            target.health = target.health - damage
            self.sp -= 50

    def Sexy_Wink(self,target): # Decreases target armour and increases hero's evasion 
        attack_name = "Sexy Wink"
        if target.armour[1] > target.armour[0]:  
            target.armour[1] = target.armour[1] - 1
            self.evasion[1] = self.evasion[1] + 4
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} gets the message and strips of some armour, {self.name} feels swifty")
        else:
            print(f"{target.name} has no more armour to strip!")
        self.sp -= 15

    def Glob_of_Glue(self,target): # Decreases target armour, but also increases target attack
        attack_name = "Glob of Glue"
        if target.evasion[1] > target.evasion[0]:  
            target.evasion[1] = round(target.evasion[1] * 0.6)
        target.attack[1] = round(target.attack[1] * 1.1)
        print(f"\n {self.name} uses {attack_name} on {target.name}.")
        print(f"{target.name} is stuck, but {target.name} also feels annoyed")
        self.sp -= 10       

    def Armour_Up(self,target): # Boosts hero's armour 
        attack_name = "Armour Up"
        self.armour = [self.armour[0],self.armour[1] + 2] #Maybe boosts are too powerful
        print(f"\n{self.name} uses {attack_name} and gets more armour")
        self.sp -= 10
        
    def Evasive_Boost(self,target): # Boosts hero's evasion
        attack_name = "Evasive Boost"
        self.evasion = [self.evasion[0],self.evasion[1] + 8] #Maybe boosts are too powerful
        print(f"\n{self.name} uses {attack_name} and feels swifty.")
        self.sp -= 10
        
    def Heal(self,target): # Heals hero
        attack_name = "Heal"
        base_stats = open_hero()
        heal = round(base_stats.health / 5)
        if (heal + self.health) > base_stats.health:
            self.health = base_stats.health
        else:
            self.health += heal
        print(f"\n{self.name} uses {attack_name} and heals for {heal} HP.")
        self.sp -= 20


##### skill end #########################################################
    def Level_Up(self):
        
        if self.experience >= 30:
            self.level = self.level + 1
            print(f"\nPlayer leveled up! Your level is now {self.level}\n")
            time.sleep(1)
            print("Enter 1 - (+ 1 to strength)")
            print("Enter 2  - (+ 1 to dexterity)")
            x = int(str(msvcrt.getch()).strip("b").strip("'"))
            while True:
                if x == 1:
                    print(f"Your strength went up from {self.str} to {self.str + 1}!")
                    self.str = self.str + 1
                    break
                elif x == 2:
                    print(f"Your dexterity went up from {self.dex} to {self.dex + 1}!")
                    self.str = self.dex + 1
                    break
                else:
                    print("incorrect input")
            time.sleep(1.5)
            os.system("cls")
            choices = []
            while len(choices) < 3:
                choice = random.choice(self.all_skills)
                if choice in self.skills or choice in choices:
                    pass
                else:
                    choices.append(choice)
            
            if len(self.skills)>=4:
                while True:
                    userin = input("You can only have four skills, do you want to remove one to learn another? y/n").lower()
                    if userin == "y" or userin == "n":
                        break
                    else:
                        print("incorrect input")
                if userin == "y":
                    for i in range(len(self.skills)):
                        print(f"Enter {i} to unlearn {self.skills[i]}")
                    while True:
                        x = int(input())
                        if x <= 0 or x >= 4:
                            break
                        else:
                            print("incorrect input")
                    #remover = int(input(f"Which skill do you want removed:\n1:{self.skills[0]}\n2:{self.skills[1]}\n3:{self.skills[2]}\n4:{self.skills[3]}\n: "))-1
                    print(f"You have unlearned {self.skills[x]}")
                    del(self.skills[x])
                    time.sleep(1)
                    os.system("cls")
                    print("You can learn a new skill!\n")
                    while True:
                        for i in range(len(choices)):
                            print(f"Enter {i+1} to learn {choices[i]}")
                        user_choice = int(input())-1
                        if user_choice == 0 or user_choice == 1 or user_choice == 2:
                            break
                        else:
                            print("incorrect input")
                else:
                    pass
            else: 
                print("You can learn a new skill!")
                while True:
                    for i in range(len(choices)):
                        print(f"Enter {i+1} to learn {choices[i]}")
                    user_choice = int(input())-1
                    if user_choice == 0 or user_choice == 1 or user_choice == 2:
                        break
                    else:
                        print("incorrect input")
            self.experience = 0

            
        
        
        
        
    

        

# monster class, (Simon, Aaron)
class Monster(Hero):
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.attack = [1,10]
        self.armour = [1,10]
        self.evasion = [1,10]
        self.skills = ["Bash", "Doom", "Enrage","Deenergize"] # At the moment Monsters start with all skills
                                                                 # If we want more skills, we can make skill randomizer function

    def Bash(self, target):
        damage = random.randint(self.attack[0], self.attack[1]) - random.randint(target.armour[0], target.armour[1])
        if damage < 0:
            damage = 0
      
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            print(f"{self.name} uses Bash on {target.name}.")
            print(f"You dodged the attack!")
        else:
            print(f"{self.name} uses attack on {target.name}.")
            print(f"You took {damage} damage!")
            target.health = target.health - damage


    def Doom(self,target): # A 2% chance to bring Hero's HP down to 1
        attack_name = "Doom"
        x = random.randint(1,100)

        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            print(f"{self.name} uses attack on {target.name}.")
            print(f"You dodged the attack!")
        else:
            print(f"{self.name} uses {attack_name} on {target.name}.")
            if x >= 99:
            
                print(f"You were hit by utter despair!")
            
                target.health = 1
            else:
                print("You were not doomed this time!")

    def Enrage(self,target): # Boosts monster max damage by approx 20%
        attack_name = "Enrage"
        print(f"{self.name} uses {attack_name} and is raging mad!\nDamage increases")
        self.attack[1] += round(self.attack[1]/5)

    def Deenergize(self,target): # Does half amout of normal damage, but saps Hero's SP
        attack_name = "Deenergize"
        damage = random.randint(self.attack[0], self.attack[1]) - random.randint(target.armour[0], target.armour[1])/2
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} took {damage} damage!")
            target.health = target.health - damage
            target.sp -= 20  
#proposal to call menu as an option
def menu():
    os.system("cls")
    player = open_hero()
    print("Menu")
    print("Enter: 1 - New Game, 2 - Continue, 3 - Save, 4 - Character Data, 5 - Save and Quit")

    x = str(msvcrt.getch()).strip("b").strip("'")
    if x == "1":
        NewGame()
    elif x == "2":
        Continue()
    elif x == "3":
        save(player)
    elif x == "4":
        CharacterData(player)
    elif x == "5":
        savequit(player)
    else:
        print("Incorrect input, please enter 1, 2, 3, 4, or 5")
        menu()


#continue menu
def Continue():
    player = open_hero()
    print("Enter: 1 - Battle  2 - Main Menu  3 - Character Information  4 - Save and Quit")
    x = str(msvcrt.getch()).strip("b").strip("'")
    if x == "1":
        battle()
    elif x == "2":
        menu()
    elif x == "3":
        CharacterData(player)
    elif x == "4":
        savequit(player)
    else:
        print("Incorrect input, please enter 1, 2, 3, or 4")
        Continue()

#prints character info, (Simon, Aaron)
def CharacterData(hero):
    os.system("cls")
    print(f"Name: {hero.name}")
    print(f"Level: {hero.level}")
    print(f"Health: {hero.health}")
    print(f"Attack: {hero.attack[0]}" + "-" + f"{hero.attack[1]}")
    print(f"Armour: {hero.armour[0]}" + "-" + f"{hero.armour[1]}")
    print(f"Evasion: {hero.evasion[0]}" + "-" + f"{hero.evasion[1]}")
    print(f"SP: {hero.sp}")

    print(f"Strength: {hero.str}")
    print(f"Dexterity: {hero.dex}")
    print(f"Skills: {hero.skills}")
    Continue()


""" def save(hero):
    x = open("/hero.txt", "w")
    x.write(f"{hero.name},")
    x.write(f"{hero.level},")
    x.write(f"{hero.experience},")
    x.write(f"{hero.health},")
    x.write(f"{hero.attack},")
    x.write(f"{hero.armour},")
    x.write(f"{hero.evasion},")
    x.write(f"{hero.str},")
    x.write(f"{hero.dex},")
    x.write(f"{hero.skills},") """

#saving hero as a json file
def save(hero):
    os.system("cls")
    hero_info = {}
    hero_info["name"] = hero.name 
    hero_info["level"] = hero.level
    hero_info["experience"] = hero.experience
    hero_info["health"] = 100 + (50*hero.str) + (50*hero.dex)
    hero_info["attack"] = [(5 + (5*hero.str) + (5*hero.dex)),(10 + (5*hero.str) + (5*hero.dex))]
    hero_info["armour"] = [(1 + (5*hero.str)), (10 + (5*hero.str))]
    hero_info["evasion"] = [(1 + (5*hero.dex)), (10 + (5*hero.dex))]
    hero_info["sp"] = 40 + (10*hero.dex)
    hero_info["str"] = hero.str
    hero_info["dex"] = hero.dex
    hero_info["skills"] = hero.skills
    hero_info["highscore"] = hero.highscore
    hero_info["turns"] = hero.turns
    with open("hero.json", "w") as outfile:
        json.dump(hero_info, outfile, indent=3)
    Continue()

def savequit(hero):
    hero_info = {}
    hero_info["name"] = hero.name 
    hero_info["level"] = hero.level
    hero_info["experience"] = hero.experience
    hero_info["health"] = 100 + (50*hero.str) + (50*hero.dex)
    hero_info["attack"] = [(5 + (5*hero.str) + (5*hero.dex)),(10 + (5*hero.str) + (5*hero.dex))]
    hero_info["armour"] = [(1 + (5*hero.str)), (10 + (5*hero.str))]
    hero_info["evasion"] = [(1 + (5*hero.dex)), (10 + (5*hero.dex))]
    hero_info["sp"] = 40 + (10*hero.dex)
    hero_info["str"] = hero.str
    hero_info["dex"] = hero.dex
    hero_info["skills"] = hero.skills
    hero_info["highscore"] = hero.highscore
    hero_info["turns"] = hero.turns
    with open("hero.json", "w") as outfile:
        json.dump(hero_info, outfile, indent=3)


#opens hero and returns it
def open_hero():
    hero = Hero()
    with open("hero.json") as infile:
        hero_data = json.load(infile)
        hero.name = hero_data["name"]
        hero.level = hero_data["level"]
        hero.experience = hero_data["experience"]
        hero.health = hero_data["health"]
        hero.attack = hero_data["attack"]
        hero.armour = hero_data["armour"]
        hero.evasion = hero_data["evasion"]
        hero.sp = hero_data["sp"]
        hero.str = hero_data["str"]
        hero.dex = hero_data["dex"]
        hero.skills = hero_data["skills"]
        hero.highscore = hero_data["highscore"]
        hero.turns = hero_data["turns"]
    return hero

#opens middle boss
def open_midboss():
    midboss = Monster("e")
    with open("midboss.json") as infile:
        monster_data = json.load(infile)
        midboss.name = monster_data["name"]
        midboss.health = monster_data["health"]
        midboss.attack = monster_data["attack"]
        midboss.armour = monster_data["armour"]
        midboss.evasion = monster_data["evasion"]
        midboss.sp = monster_data["sp"]
        midboss.skills = monster_data["skills"]
    return midboss

#opens final boss
def open_finalboss():
    finalboss = Monster("e")
    with open("finalboss.json") as infile:
        monster_data = json.load(infile)
        finalboss.name = monster_data["name"]
        finalboss.health = monster_data["health"]
        finalboss.attack = monster_data["attack"]
        finalboss.armour = monster_data["armour"]
        finalboss.evasion = monster_data["evasion"]
        finalboss.sp = monster_data["sp"]
        finalboss.skills = monster_data["skills"]
    return finalboss

#creates midboss
def midboss():
    monster_info = {}
    monster_info["name"] = "Soul King"
    monster_info["health"] = 250
    monster_info["attack"] = [1,20]
    monster_info["armour"] = [1,20]
    monster_info["evasion"] = [1,15]
    monster_info["sp"] = 500
    monster_info["skills"] = ["Bash", "Doom", "Enrage","Deenergize"]
    with open("midboss.json", "w") as outfile:
        json.dump(monster_info, outfile, indent=3)

def bossend1():
    monster_info = {}
    monster_info["name"] = "Soul King"
    monster_info["health"] = 0
    monster_info["attack"] = [1,20]
    monster_info["armour"] = [1,20]
    monster_info["evasion"] = [1,15]
    monster_info["sp"] = 500
    monster_info["skills"] = ["Bash", "Doom", "Enrage","Deenergize"]
    with open("midboss.json", "w") as outfile:
        json.dump(monster_info, outfile, indent=3)

#creates final boss
def finalboss():
    monster_info = {}
    monster_info["name"] = "Dungeon Master"
    monster_info["health"] = 400
    monster_info["attack"] = [1,30]
    monster_info["armour"] = [1,30]
    monster_info["evasion"] = [1,20]
    monster_info["sp"] = 500
    monster_info["skills"] = ["Bash", "Doom", "Enrage","Deenergize"]
    with open("finalboss.json", "w") as outfile:
        json.dump(monster_info, outfile, indent=3)

def bossend2():
    monster_info = {}
    monster_info["name"] = "Dungeon Master"
    monster_info["health"] = 0
    monster_info["attack"] = [1,30]
    monster_info["armour"] = [1,30]
    monster_info["evasion"] = [1,20]
    monster_info["sp"] = 500
    monster_info["skills"] = ["Bash", "Doom", "Enrage","Deenergize"]
    with open("finalboss.json", "w") as outfile:
        json.dump(monster_info, outfile, indent=3)

#Does the mid boss battle
def bossbattle(origin,player,boss,final):
    final = final
    print("Boss Alert")
    print(f"You are fighting {boss.name}")
    while player.health >= 0 and boss.health >= 0:
        origin.turns += 1
        #print(f"Your skills {player.skills}")
        skill_list = len(player.skills)
        for i in range(skill_list):
            print(f"\nEnter {i + 1} to use {player.skills[i]}")
        try:
            y = int(str(msvcrt.getch()).strip("b").strip("'")) - 1
        except:
            print("incorrect input")
            continue
        os.system("cls")
        #since eval() is being used, this is for security reasons
        if y >=0 and y <= 10:
            try:
                if player.sp <= 0:  # Introduces SP system, heroes can go to minus SP, but will then only be able to perform basic attacks
                    print('You are out of SP, can only perform basic attack')
                    player.Attack(boss)
                else:
                    eval(f"player.{player.skills[y]}(boss)") #player.tackle(boss)
            except:
                print("incorrect input")
                continue
        else:
            print("incorrect input")
            continue
        x = random.randint(0,len(boss.skills)-1) # Random choice for boss skills
        eval(f"boss.{boss.skills[x]}(player)")
        player.sp += 10
        print(f"Player HP: {player.health}\nPlayer SP: {player.sp}")
        print(f"boss HP: {boss.health}")
        
    if player.health <= 0:
        print("You died")
        print(f"Your highscore is {origin.highscore}")
        print("New Game? y/n")
        while True:
            x = str(msvcrt.getch()).strip("b").strip("'")
            if x == "y":
                NewGame()
            elif x == "n":
                origin = Hero()
                savequit(origin)
                print("See you next time")
                sys.exit()
    else:
        if final == True:
            origin.highscore = origin.highscore + (10000/origin.turns)
            print("You won the game")
            print(f"Your High Score is {origin.highscore}")
            print("\n New Game? y/n")
            while True:
                x = str(msvcrt.getch()).strip("b").strip("'")
                if x == "y":
                    NewGame()
                elif x == "n":
                    print("See You Again")
                    origin = Hero()
                    savequit(origin)
                    sys.exit()
                else:
                    print("incorrect Input")
        else:
            print(f"You defeated {boss.name} and gained 30 experience")
            origin.experience = origin.experience + 30
            origin.highscore = origin.highscore + (5000/origin.turns)
            origin.turns = 0
            bossend1()
            origin.Level_Up()
            save(origin)

#battle simulation, (Simon, Aaron)
def battle():
    #generates monster name
    monster_name = ["Ice", "Flame", "Stone"]
    monster_name2 = ["Golem", "Slime", "Wolf"]
    fullname = monster_name[random.randint(0,2)] + " " + monster_name2[random.randint(0,2)]
    #initiates player
    origin = open_hero()   
    player = open_hero()
    monster = Monster(fullname)

    #Monster Scaling in intervals (we can make this simpler by scaling by level)
    if player.level >= 2 and player.level <= 4:
        monster.health = 100
        monster.attack = [3,12]
        monster.armour = [3,12]
        monster.evasion = [1,10]
    elif player.level >= 4 and player.level <= 6:
        monster.health = 200
        monster.attack = [3,14]
        monster.armour = [3,14]
        monster.evasion = [5,15]
    elif player.level >= 6 and player.level <= 8:
        monster.health = 250
        monster.attack = [5,15]
        monster.armour = [5,15]
        monster.evasion = [5,15]
    elif player.level >= 8:
        monster.health = 250
        monster.attack = [7,17]
        monster.armour = [7,17]
        monster.evasion = [7,17]
    if player.level >= 5:
        midboss = open_midboss()
        print(midboss.health)
        if midboss.health > 0:
            print("Fight the mid-dungeon boss?")
            print("Enter: y or n")
            x = str(msvcrt.getch()).strip("b").strip("'")
            if x == "y":
                bossbattle(origin,player,midboss,False)
                pass
        elif midboss.health <= 0 and player.level >= 10:
            finalboss = open_finalboss()
            print("Would you like to fight the Final boss?")
            print("Enter: y or n")
            while True:
                x = str(msvcrt.getch()).strip("b").strip("'")
                if x == "y":
                    bossbattle(origin,player,finalboss,True)
                elif x == "n":
                    break
                else:
                    print("incorrect input")
    os.system("cls")
    print(f"You have entered battle against {monster.name}!")
    time.sleep(1.5)
    print(" ")
    while player.health > 0 and monster.health > 0:
        origin.turns += 1
        #print(f"Your skills {player.skills}")
        skill_list = len(player.skills)
        for i in range(skill_list):
            print(f"\nEnter {i + 1} to use {player.skills[i]}")
        try:
            y = int(str(msvcrt.getch()).strip("b").strip("'")) - 1
        except:
            print("incorrect input")
            continue
        os.system("cls")
        #since eval() is being used, this is for security reasons
        if y >=0 and y <= 10:
            try:
                if player.sp <= 0:  # Introduces SP system, heroes can go to minus SP, but will then only be able to perform basic attacks
                    print('You are out of SP, can only perform basic attack')
                    player.Attack(monster)
                else:
                    eval(f"player.{player.skills[y]}(monster)") #player.tackle(monster)
            except:
                print("incorrect input")
                continue
        else:
            print("incorrect input")
            continue
        x = random.randint(0,len(monster.skills)-1) # Random choice for monster skills
        eval(f"monster.{monster.skills[x]}(player)")
        player.sp += 10
        print(f"Player HP: {player.health}\nPlayer SP: {player.sp}")
        print(f"Monster HP: {monster.health}")
        
    if player.health <= 0:
        print("You died")
        print(f"Your highscore is {origin.highscore}")
        print("New Game? y/n")
        while True:
            x = str(msvcrt.getch()).strip("b").strip("'")
            if x == "y":
                NewGame()
            elif x == "n":
                player = Hero()
                savequit(player)
                print("See you next time")
    else:
        print(f"You defeated {monster.name} and gained 30 experience")
        origin.experience = origin.experience + 30
        if origin.highscore >= origin.turns:
            origin.highscore = origin.highscore + (500/origin.turns)
        origin.Level_Up()
       
        #save also continues the game
        save(origin)

    

        
    
        


    #battle takes place
    #if player levels up to 2, 4, 6
        #skills = ["Tackle", "Megaburst"]
        #Choose betwen skills
        #Player chooses tacke
        #player.skills = [tackle()]

    


#tackle()

#Enter: 1 - Attack, 2 - Defend 

#creates skill table to learn skills



###Simulates attack, (Simon, Aaron)
##def Attack(player, target):
##    #calculates damage
##    attack_name = "Attack"
##    damage = random.randint(player.attack[0], player.attack[1]) - random.randint(target.armour[0], target.armour[1])
##    #if armour is higher than damage, damage = 0
##    if damage < 0:
##        damage = 0
##    #calculates if enemy dodged
##    if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
##        print(f"\n {player.name} uses {attack_name} on {target.name}.")
##        print(f"{target.name} dodged the attack!")
##    else:
##        print(f"\n{player.name} uses {attack_name} on {target.name}.")
##        print(f"{target.name} took {damage} damage!")
##        target.health = target.health - damage



def m_Attack(enemy, target):
    #calculates damage
    damage = random.randint(enemy.attack[0], enemy.attack[1]) - random.randint(target.armour[0], target.armour[1])
    #if armour is higher than damage, damage = 0
    if damage < 0:
        damage = 0
    #calculates if enemy dodged
    if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
        print(f"{enemy.name} uses attack on {target.name}.")
        print(f"You dodged the attack!")
    else:
        print(f"{enemy.name} uses attack on {target.name}.")
        print(f"You took {damage} damage!")
        target.health = target.health - damage



"""
x = Hero()
x.name = "Arnold"
y = Monster("Apple")
save(x)
open_hero()
m = "Tackle"
z = eval(f"{m}(x,y)")
"""

#checks if there is save data.

"""
try:
    hero = open("hero.json")
    try:
        try:
            player = Hero()
            if player == hero:
                NewGame()
            else:
                Continue()
        except:
            sys.exit(0)
    except:
        print("exiting...")
#no save data, so new game
except:
    print("here?")
    NewGame()
"""

Continue()