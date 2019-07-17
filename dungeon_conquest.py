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
                #input()
                #You can choose one new skill
                    #pickbetween one or two
                #
            #save player data in to text file

#skills
#Tutorial (NewGame())
#high score (points for winning battle relative to level)
#turn counter. more points for beating it quickly
#limit on skills (uses?)
#monster uses a random one of 1-4 skills


import random
import time
import json
import os


def NewGame():
    print("Welcome to ____")
    print("Please enter your Character name")
    x = str(input())
    player = Hero()
    player.name = x
    print(f"Welcome {player.name}")
    #Below here are the instructions to the game
    print("")
    save(player)

# hero class, (Simon, Aaron)
class Hero:
    def __init__(self):
        self.name = ""
        self.level = 1
        self.experience = 0
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
        if self.level == target.level and self.str == target.str and self.dex == target.dex and self.name == target.name:
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
            target.health = target.health - damage

    def Thrust(self,target):
        attack_name = "Thrust"
        damage = random.randint(self.attack[0], self.attack[1]) - random.randint(target.armour[0], target.armour[1] - self.attack[0])
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            
            
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name}'s armour was pierced for {damage} damage!")
            target.health = target.health - damage
        self.sp = self.sp - 10

    def Armour_Breaker(self,target):
        attack_name = "Armour Breaker"
        damage = random.randint(self.attack[0]*0.5, self.attack[1]*0.5) - random.randint(target.armour[0], target.armour[1])
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name}'s armour was thrashed for {damage} damage!")
            target.health = target.health - damage
            target.armour[1] = target.armour[1] - damage

    def Tendon_Cut(self,target):
        attack_name = "Tendon Cut"
        damage = random.randint(self.attack[0]*0.5, self.attack[1]*0.5) - random.randint(target.armour[0], target.armour[1])
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(0,100):
            
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name}'s tendons were cut for {damage} damage!")
            target.health = target.health - damage
            target.evasion[1] = target.evasion[1] * 0.80

    def Berserker_slash(self,target):
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
            self.health -= (damage/5)
            target.health = target.health - damage

    def Sacrifice(self,target):
        attack_name = "Sacrifice"
        damage = random.randint(self.attack[0]*10, self.attack[1]*10) - random.randint(target.armour[0], target.armour[1])
        if damage < 0:
            damage = 0
        if random.randint(target.evasion[0], target.evasion[1]) >= random.randint(60,100):
            
            print(f"\n {self.name} uses {attack_name} on {target.name}.")
            print(f"{target.name} dodged the attack!")
        else:
            
            print(f"\n{self.name} uses {attack_name} on {target.name}.")
            print(f"""{self.name} knows the true meaning of sacrifice"\
                  {target.name} took {damage} damage in an all out attack, but {self.name} was severly hurt by the attack!""")
            self.health -= (self.health * 0.5)
            target.health = target.health - damage

    def Sexy_Wink(self,target):
        attack_name = "Sexy Wink"
        target.armour[1] = target.armour[1] - 1
        self.evasion[1] = self.evasion[1] + 1
        print(f"\n {self.name} uses {attack_name} on {target.name}.")
        print(f"{target.name} gets the message and strips of some armour, {self.name} feels swifty")
        self.sp = self.sp - 10

    def Glob_of_Glue(self,target):
        attack_name = "Glob of Glue"
        target.evasion[1] = target.evasion[1] * 0.6
        target.attack[1] = target.attack[1] * 1.1
        print(f"\n {self.name} uses {attack_name} on {target.name}.")
        print(f"{target.name} is stuck, but {target.name} also feels annoyed")
               

    def Armour_Up(self):
        attack_name = "Armour Up"
        self.armour = [self.armour[0] * 1.5,self.armour[1] * 1.5] #Maybe boosts are too powerful, but minimum boost can be removed if so.
        print(f"\n{self.name} uses {attack_name} and gets more armour")

    def Evasive_Boost(self):
        attack_name = "Evasive Boost"
        self.evasion = [self.evasion[0] * 1.2,self.evasion[1] * 1.2] #Maybe boosts are too powerful, but minimum boost can be removed if so.
        print(f"\n{self.name} uses {attack_name} and feels swifty.")

    def Heal(self):
        attack_name = "Heal"
        base_stats = open_hero()
        heal = base_stats.health * 0.20
        if (heal + self.health) > base_stats.health:
            self.health = base_stats.health
        else:
            self.health += heal
        print(f"\n{self.name} uses {attack_name} and heals for {heal} HP.")


##### skill end #########################################################
    def Level_Up(self):
        if self.experience >= 30:
            self.level = self.level + 1
            print(f"Player leveled up! Your level is now {self.level}")
            print("Enter 1 for one point in strength")
            print("Enter 2 for one point in dexterity")
            x = int(input())
            if x == 1:
                print(f"Your strength went up from {self.str} to {self.str + 1}!")
                self.str = self.str + 1
            if x == 2:
                print(f"Your dexterity went up from {self.dex} to {self.dex + 1}!")
                self.str = self.dex + 1
            choices = []
            while len(choices) < 2:
                choice = random.choice(self.all_skills)
                if choice in self.skills or choice in choices:
                    pass
                else:
                    choices.append(choice)
            
            print("You can learn new skills!")
            user_choice = int(input(f"Pick 1:{choices[0]} or 2:{choices[1]}: "))-1
            if len(self.skills)>=4:
                userin = input("You can only have four skills, do you want to remove one?: ").lower()
                if userin == "yes":
                    remover = int(input(f"""Which skill do you want removed: 1:{self.skills[0]}, 2:{self.skills[1]}, 3:{self.skills[2]} or"\
                                    4:{self.skills[3]}: """))-1
                    del(self.skills[remover])
                    self.skills.append(choices[user_choice])
                else:
                    pass
            else:
                     
                self.skills.append(choices[user_choice])
            
            self.experience = 0

            
        
        
        
        
    

        

# monster class, (Simon, Aaron)
class Monster(Hero):
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.attack = [1,10]
        self.armour = [1,10]
        self.evasion = [1,10]
        self.sp = 500
        self.skills = ["m_Attack"]


#proposal to call menu as an option
def menu():
    player = open_hero()
    print("Menu")
    print("Enter: 1 - New Game, 2 - Continue, 3 - Save, 4 - Character Data, 5 - Save and Quit")

    x = input()
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
    x = input()
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
    print(hero.name)
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
    hero_info = {}
    hero_info["name"] = hero.name
    hero_info["level"] = hero.level
    hero_info["experience"] = hero.experience
    hero_info["health"] = hero.health
    hero_info["attack"] = hero.attack
    hero_info["armour"] = hero.armour
    hero_info["evasion"] = hero.evasion
    hero_info["sp"] = hero.sp
    hero_info["str"] = hero.str
    hero_info["dex"] = hero.dex
    hero_info["skills"] = hero.skills
    with open("hero.json", "w") as outfile:
        json.dump(hero_info, outfile, indent=3)
    Continue()

def savequit(hero):
    hero_info = {}
    hero_info["name"] = hero.name
    hero_info["level"] = hero.level
    hero_info["experience"] = hero.experience
    hero_info["health"] = hero.health
    hero_info["attack"] = hero.attack
    hero_info["armour"] = hero.armour
    hero_info["evasion"] = hero.evasion
    hero_info["sp"] = hero.sp
    hero_info["str"] = hero.str
    hero_info["dex"] = hero.dex
    hero_info["skills"] = hero.skills
    with open("hero.json", "w") as outfile:
        json.dump(hero_info, outfile, indent=3)
    Continue()

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
    monster_info["health"] = 500
    monster_info["attack"] = [1,100]
    monster_info["armour"] = [1,100]
    monster_info["evasion"] = [1,50]
    monster_info["sp"] = 500
    monster_info["skills"] = ["m_Tackle"]
    with open("midboss.json", "w") as outfile:
        json.dump(monster_info, outfile, indent=3)

#creates final boss
def finalboss():
    monster_info = {}
    monster_info["name"] = "Dungeon Master"
    monster_info["health"] = 1000
    monster_info["attack"] = [1,200]
    monster_info["armour"] = [1,200]
    monster_info["evasion"] = [1,100]
    monster_info["sp"] = 500
    monster_info["skills"] = ["m_Tackle"]
    with open("finalboss.json", "w") as outfile:
        json.dump(monster_info, outfile, indent=3)



#battle simulation, (Simon, Aaron)
def battle():
    lost = False
    #generates monster name
    monster_name = ["Ice", "Flame", "Stone"]
    monster_name2 = ["Golem", "Slime", "Wolf"]
    fullname = monster_name[random.randint(0,2)] + " " + monster_name2[random.randint(0,2)]
    #initiates player
    origin = open_hero()   
    player = open_hero()
    monster = Monster(fullname)

    
    print(f"You have entered battle against {monster.name}!")

    #Monster Scaling in intervals (we can make this simpler by scaling by level)
    if player.level >= 2 and player.level <= 4:
        monster.health = 100
        monster.attack = [1,20]
        monster.armour = [1,20]
        monster.evasion = [1,10]
    elif player.level >= 4 and player.level <= 6:
        monster.health = 200
        monster.attack = [1,30]
        monster.armour = [1,30]
        monster.evasion = [1,20]
    elif player.level >= 6 and player.level <= 8:
        monster.health = 250
        monster.attack = [1,40]
        monster.armour = [1,40]
        monster.evasion = [1,30]
    elif player.level >= 8:
        monster.health = 250
        monster.attack = [1,50]
        monster.armour = [1,50]
        monster.evasion = [1,30]
    if player.level >= 5:
        midboss = open_midboss()
        if midboss.health > 0:
            print("Fight the mid-dungeon boss?")
            print("Enter: y or n")
        elif midboss.health <= 0 and player.level >= 10:
            finalboss = open_finalboss()
            print("Would you like to fight the Final boss?")
            print("Enter: y or n")
    while player.health > 0 and monster.health > 0:
        #print(f"Your skills {player.skills}")
        skill_list = len(player.skills)
        for i in range(skill_list):
            print(f"\nEnter {i + 1} to use {player.skills[i]}")
        try:
            y = int(input()) - 1
        except:
            print("incorrect input")
            continue
        #since eval() is being used, this is for security reasons
        if y >=0 and y <= 10:
            try:
                eval(f"player.{player.skills[y]}(monster)") #player.tackle(monster)
            except:
                print("incorrect input")
                continue
        else:
            print("incorrect input")
            continue
        m_Attack(monster, player)
        player.sp += 10
        print(f"Player HP: {player.health}\nPlayer SP: {player.sp}")
        print(f"Monster HP: {monster.health}")
        
    if player.health <= 0:
        print("You died")
        print("Your high score is _____")
        print("New Game? y/n")
        while True:
            x = input()
            if x == "y":
                NewGame()
            elif x == "n":
                player = Hero()
                save(player)
                print("See you next time")
    else:
        print(f"You defeated {monster.name} and gained 30 experience")
        origin.experience = origin.experience + 30
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


#Simulates Monster Attack, (Simon, Aaron)
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
try:
    hero = open("hero.json")
    player = Hero()
    if player == hero:
        NewGame()
    Continue()
#no save data, so new game
except:
    NewGame()
