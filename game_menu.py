if __name__ == '__main__':
    try:
        hero = open("/hero.txt")
        game = True
    except:
        #NewGame()
        print("Welcome to Dungeon Conquest")
        x = input("Please enter your Character name")
        player = Hero(x)
        print(f"Welcome {hero.name}")
        #Below here are the instructions to the game
        print("")
        game = True
    while game == True:
        print("Menu")
        option = input("Enter options '1 - 5':")
        print("1 - New Game")
        print("2 - Continue")
        print("3 - Save")
        print("4 - Character Data")
        print("5 - Save and Quit")

        
        if option == "1": # New Game 
            print("Welcome to Dungeon Conquest")
            x = input("Please enter your Character name")
            player = Hero(x)
            print(f"Welcome {hero.name}")
            #Below here are the instructions to the game
            print("")
            game = True
                
        elif option == "2": # Continue
            hero_name = input("What's your hero's name?")
            print("Welcome back, ", hero_name)
            # retrieve data from saved file
            open_hero(hero_name)
               
            # display game menu
            hero = True
            while hero == True:
                option = input("Enter options 1 - 4:")
                print("1 - Battle")
                print("2 - Main Menu")
                print("3 - Character Information")
                
                if option == "1": # Battle


                    ## TBC ##

                                  
                elif option == "2": # Back to main menu
                    hero = False
                    game = True
                                  
                elif option == "3": # Display Character Information
                    CharacterData(hero.name)

                    ## ??? ##
                                  
                else:
                    print("Please enter valid option, e.g. 1, 2 etc.")
                
            
        elif option == "3": # Save


            ##TBC##


        elif option == "4": # Display Character Data


            ## ??? ##
            

        elif option == "5": # Save and quit
            game = False # Quit the loop
            
        else: # Invalid input
            print("Please enter valid option, e.g. 1, 2 etc.")
            game = True


    # shelve the data
    Save(player)


    ## TBC ##
            




    

