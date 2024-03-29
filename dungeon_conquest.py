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

#New Game, (Aaron, Alice)
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

# hero class, (Aaron, Simon)
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
        self.descriptions = {"Attack": "Basic Attack",
                           "Thrust": "An attack that ignores some of the enemey's armour",
                           "Armour_Breaker": "A weaker attack, but leaves lasting damage on enemy armour",
                           "Tendon_Cut": "A minor attack that slices enemy tendons, decreasing their evasion",
                           "Berserker_Slash": "Does 3X times the damage, but it hurts you as well",
                           "Sacrifice": "An incredibly devastating attack, but sacrifices half your health after each use",
                           "Sexy_Wink": "Decreases the enemy's armour and boosts your evasion",
                           "Glob_of_Glue": "A sticky mess that decreases the enemy's evasion, but increases their attack",
                           "Armour_Up": "Increases player armour",
                           "Evasive_Boost": "Increases player evasion",
                           "Heal": "Restores player health"}
    
    def __eq__(self, target):
        if self.name == target.name:
            return True
        else:
            return False
##### skill start #####################################################

    #Skills, Simon
    def Attack(self, target):
        
    #calculates damage
        attack_name = "Attack"
        damage = random.randint(self.attack[0], self.attack[1]) - random.randint(target.armour[0], target.armour[1])
    #if armour is higher than damage, damage = 0
        if damage < 0:
            damage = 0
    #calculates if enemy dodged
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} took {damage} damage!")
            target.health = target.health - damage

    def Thrust(self,target):  # Same as attack, but ignores some of the target's armour
        attack_name = "Thrust"
        damage = random.randint(self.attack[0], self.attack[1]) - random.randint(target.armour[0], target.armour[1] -2)
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
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
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
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
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name}'s tendons were cut for {damage} damage, reducing their evasion by 20%!")
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
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} was brutally slashed for {damage} damage, but {self.name} was hurt by the attack and lost 25% HP!")
            self.health -= (self.health * 0.25)
            target.health = target.health - damage
            self.sp -= 20

    def Sacrifice(self,target): # Does 10 times the damage of attack, but uses half of hero health
        attack_name = "Sacrifice"
        damage = random.randint(self.attack[0]*10, self.attack[1]*10) - random.randint(target.armour[0], target.armour[1])
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(60,100):
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"""{self.name} knows the true meaning of sacrifice"
                  \n{target.name} took {damage} damage in an all out attack, but {self.name} was severly hurt by the attack!""")
            self.health -= round((self.health * 0.5))
            target.health = target.health - damage
            self.sp -= 50

    def Sexy_Wink(self,target): # Decreases target armour and increases hero's evasion 
        attack_name = "Sexy Wink"
        if target.armour[1] > target.armour[0]:  
            target.armour[1] = target.armour[1] - 1
            self.evasion[1] = self.evasion[1] + 4
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} gets the message and strips of some armour, {self.name} feels swifty")
        else:
            print(f"{target.name} has no more armour to strip!")
        self.sp -= 15

    def Glob_of_Glue(self,target): # Decreases target armour, but also increases target attack
        attack_name = "Glob of Glue"
        if target.evasion[1] > target.evasion[0]:  
            target.evasion[1] = round(target.evasion[1] * 0.6)
        target.attack[1] = round(target.attack[1] * 1.1)
        print(f"\n{self.name} uses {attack_name} on {target.name}.")
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
    #Level up, (Simon, Aaron)
    def Level_Up(self):
        
        if self.experience >= 30:
            self.level = self.level + 1
            print(f"You leveled up to level {self.level}!\n")
            time.sleep(0.2)
            print("Enter 1 - (+ 1 to strength)")
            print("Enter 2  - (+ 1 to dexterity)")
            x = int(str(msvcrt.getch()).strip("b").strip("'"))
            os.system("cls")
            while True:
                if x == 1:
                    print(f"\nYour strength went up from {self.str} to {self.str + 1}!\n")
                    self.str = self.str + 1
                    break
                elif x == 2:
                    print(f"\nYour dexterity went up from {self.dex} to {self.dex + 1}!\n")
                    self.str = self.dex + 1
                    break
                else:
                    print("incorrect input")
            time.sleep(.5)
            choices = []
            while len(choices) < 3:
                choice = random.choice(self.all_skills)
                if choice in self.skills or choice in choices:
                    pass
                else:
                    choices.append(choice)
            
            if len(self.skills)>=4:
                print("You can only have up to four skills!")
                print("Would you like to unlearn a skill to learn another? y/n\n")
                while True:
                    userin = str(msvcrt.getch()).strip("b").strip("'")
                    if userin == "y" or userin == "n":
                        break
                    else:
                        print("incorrect input")
                if userin == "y":
                    for i in range(len(self.skills)):
                        s_name = self.skills[i].split("_")
                        s_name = " ".join(s_name)
                        print(f"Enter {i+1} to unlearn {s_name}")
                    while True:
                        x = int(str(msvcrt.getch()).strip("b").strip("'")) - 1
                        if x >= 0 and x <= 4:
                            break
                        else:
                            print("incorrect input")
                    s_name = self.skills[x].split("_")
                    s_name = " ".join(s_name)
                    print(f"\nYou have unlearned {s_name}")
                    del(self.skills[x])
                    time.sleep(1.25)
                    os.system("cls")
                    print("You can learn a new skill!\n")
                    while True:
                        for i in range(len(choices)):
                            s_name = choices[i].split("_")
                            s_name = " ".join(s_name)
                            print(f"Enter {i+1} to learn {s_name}: {self.descriptions[choices[i]]}")
                        user_choice = int(str(msvcrt.getch()).strip("b").strip("'")) - 1
                        if user_choice == 0 or user_choice == 1 or user_choice == 2:
                            self.skills.append(choices[user_choice])
                            break
                        else:
                            print("incorrect input")
                else:
                    pass
            else: 
                print("You can learn a new skill!")
                while True:
                    for i in range(len(choices)):
                        s_name = choices[i].split("_")
                        s_name = " ".join(s_name)
                        print(f"Enter {i+1} to learn {s_name}: {self.descriptions[choices[i]]}")
                    user_choice = int(str(msvcrt.getch()).strip("b").strip("'")) - 1
                    if user_choice == 0 or user_choice == 1 or user_choice == 2:
                        self.skills.append(choices[user_choice])
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
        self.skills = ["Bash", "Doom", "Enrage","Drain"] # At the moment Monsters start with all skills
                                                                 # If we want more skills, we can make skill randomizer function

    #Monster Skills, (Simon, Aaron)
    def Bash(self, target):
        damage = random.randint(self.attack[0], self.attack[1]) - random.randint(target.armour[0], target.armour[1])
        if damage < 0:
            damage = 0
      
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            print(f"\n{self.name} uses Bash on {target.name}.")
            print(f"You dodged the attack!")
        else:
            print(f"\n{self.name} uses bash on {target.name}.")
            print(f"You took {damage} damage!")
            target.health = target.health - damage


    def Doom(self,target): # A 5% chance to half the Hero's HP
        attack_name = "Doom"
        x = random.randint(1,100)

        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            print(f"\n{self.name} uses attack on {target.name}.")
            print(f"You dodged the attack!")
        else:
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            if x >= 96:
            
                print(f"You were hit by utter despair and lost half of your health!")
            
                target.health = target.health - round(target.health * 0.5)
            else:
                print("You were not doomed this time!")

    def Enrage(self,target): # Boosts monster max damage by approx 20%
        attack_name = "Enrage"
        print(f"\n{self.name} uses {attack_name} and is raging mad!\nMonster Damage increases by 20%")
        self.attack[0] += round(self.attack[0]/5)
        self.attack[1] += round(self.attack[1]/5)

    def Drain(self,target): # Does half amout of normal damage, but saps Hero's SP
        attack_name = "Drain"
        damage = random.randint(self.attack[0], self.attack[1]) - random.randint(target.armour[0], target.armour[1])/2
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} took {damage} damage and lost 20 SP!")
            target.health = target.health - damage
            target.sp -= 20  
#Game Menu, (Alice, Aaron)
def menu():
    os.system("cls")
    player = open_hero()
    print("Game Menu")
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


#continue menu, (Aaron, Alice)
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
    print(f"Skills: {hero.skills}\n")
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

#saving data, Aaron
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
    monster_info["skills"] = ["Bash", "Doom", "Enrage","Drain"]
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
    monster_info["skills"] = ["Bash", "Doom", "Enrage","Drain"]
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
    monster_info["skills"] = ["Bash", "Doom", "Enrage","Drain"]
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
    monster_info["skills"] = ["Bash", "Doom", "Enrage","Drain"]
    with open("finalboss.json", "w") as outfile:
        json.dump(monster_info, outfile, indent=3)

#Does the mid boss battle
#Aaron
def bossbattle(origin,player,boss,final):
    final = final
    if final == True:
        x = "This is the end of your journey."
        for i in range(4):
            os.system("cls")
            print(f"Final Boss - {boss.name}\n")
            print(x + ' - Dungeon Master')
            x += "." 
            time.sleep(1)
        print("Revel in victory or perish! - 'Dungeon Master'")
    else:
        print("Welcome to my home. - 'Soul King'")
        time.sleep(2)
        os.system("cls")
        print("Now begone! - 'Soul King'")
        time.sleep(1)
        print("\nThe Soul king draws in half your soul. Your HP is reduced by half!")
        player.health = player.health - round(player.health * 0.5)
    while player.health >= 0 and boss.health >= 0:
        origin.turns += 1
        #print(f"Your skills {player.skills}")
        skill_list = len(player.skills)
        for i in range(skill_list):
            s_name = player.skills[i].split("_")
            s_name = " ".join(s_name)
            print(f"\nEnter {i + 1} to use {s_name}")
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
        print(f"\nPlayer HP: {player.health}\nBoss HP: {boss.health}\n\nPlayer SP: {player.sp}")
        
    if player.health <= 0:
        print("You died\n")
        print(f"Your Highscore is {round(origin.highscore)}\n")
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
            print("You won the game\n")
            print(f"Your Highscore is {round(origin.highscore)}")
            print("\nNew Game? y/n")
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
    print(f"You have entered battle against a {monster.name}!")
    print(" ")
    while player.health > 0 and monster.health > 0:
        origin.turns += 1
        #print(f"Your skills {player.skills}")
        skill_list = len(player.skills)
        for i in range(skill_list):
            s_name = player.skills[i].split("_")
            s_name = " ".join(s_name)
            print(f"\nEnter {i + 1} to use {s_name}")
        try:
            y = int(str(msvcrt.getch()).strip("b").strip("'")) - 1
        except:
            print("incorrect input")
            continue
        os.system("cls")
        print(f"Monster - {monster.name}")
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
        print(f"\nPlayer HP: {player.health}\nMonster HP: {monster.health}\n\nPlayer SP: {player.sp}")
        
    if player.health <= 0:
        print("You died\n")
        print(f"Your Highscore is {round(origin.highscore)}\n")
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

    

        
    
        

#Notes--------------------
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


"""
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



"""
x = Hero()
x.name = "Arnold"
y = Monster("Apple")
save(x)
open_hero()
m = "Tackle"
z = eval(f"{m}(x,y)")
"""
#Notes End------------------------


#Aaron
#checks if there is save data.
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
