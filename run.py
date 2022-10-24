# Global variable used to function loops and validation
play_game = True


def intro():
    """
    Introduction to the game.
    Asks user for their name and then greets the player.
    Then asks the user do they want to play a game.
    If the user answers yes then the start_game function is called.
    If the user answers no the the user is called a coward and
    the back_to_start function is called.
    A while loop evaluates user input.
    Only answers allowed are Yes, Y, No, N.
    User input is stripped of white space and converted into lowercase.
    """
    print("Hi There")
    print("")
    name = input("Enter your name:   ")
    print(f'Greetings {name.capitalize()}! \nWelcome to Pauls adventure game!')
    
    while play_game:
        start = input("Would you like to play? Yes / No\n").lower().strip()
        if start == "yes" or start == "y":
            print("Great! lets play the game then")
            start_game()
        elif start == "no" or start == "n":
            print("Coward!")
            back_to_start()
        else:
            print("Invalid input. Please try again. \n")

def back_to_start():
    """
    Asks the user do they want to go back to the start of the game
    If yes then the intro runs again
    If no the user exits the programme
    """
    to_the_start = input("Would you like to go back to the start? y/n \n")
    if to_the_start.lower().strip() == "yes":
        intro()
    else:
        exit()
    

def start_game():
    """
    Starts the game
    """
    print("--------------------------------------------------------------------------")
    print("")
    print("Your running through the woods")
    print("You have been running for so long you have forgotten how long you have been running")
    print("Your feet are hurt from running so hard")
    print("")
    print("The soles of your feet are screaming")
    print("You cant keep going")
    print("")
    print("You come to a clearing in the woods and stop for a second to catch your breath")
    print("You take in your surroundings")#add more descriptions here
    print("Everything suddenly becomes more quite, you hear seaguls far to the left")
    print("")
    print("What do you do? Do you go left towards the noise or do you go right and deeper into the forest?")
    direction = input("Do you go left or right?").strip().lower()
    if direction == "left":
        sea_scenario()
    elif direction == "right":
        forest_scenario()
    else:
        print("Invalid input. Please try again. \n")
    
def sea_scenario():
    """
    Sea scenario
    """
    print("Sea")


def forest_scenario():
    """
    Forest scenario
    """
    print("Forest")

intro()
