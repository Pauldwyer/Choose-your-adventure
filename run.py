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
    print("------------------------------------------------------------------")
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
    while play_game:
        direction = input("Do you go left or right?\n").strip().lower()
        if direction == "left" or direction == "l":
            sea_scenario()
        elif direction == "right" or direction == "r":
            forest_scenario()
        else:
            print("Invalid input. Please try again. \n")
    
def sea_scenario():
    """
    Story for when you take the direction of left in the forest clearing.
    Brings the user to a hidden beach and gives the user a choice to continue or go back to the forest.

    """
    print("------------------------------------------------------------------")
    print("You take off running in the direction of the seagul noises, forgetting the pain in your feet")
    print("")
    print("You keep running, occasionly glancing over your shoulder")
    print("The hair starts to stand on the back of your neck")
    print("You have a feeling you are being chased")
    print("Why are you running ??")
    print("What did you do to that person??")
    print("Wait, what person?? Why were those people so angry??")
    print("You start to remember a little about the chase")
    print("")
    print("Murderer the people called you")
    print("")
    print("")
    print("Suddenly you are back in the current moment, the trees start to become less dense")
    print("You start to hear the ocean")
    print("You start to run faster, maybe you can find a boat and sail to safety")
    print("")
    print("")
    print("You come out of the woods into a little hidden beach")
    print("You start to hear a lady singing, the sound of the voice is like an angel from heaven")
    print("You scan the beach and at the far you can make out a lady on the rocks")
    while play_game:
        direction = input("Do you go forward and ask the lady for help or run back into the forest? Forward or back?\n").strip().lower()
        if direction == "forward" or direction == "f":
            on_the_rocks_scenario()
        elif direction == "back" or direction == "b":
            forest_clearing_scenario()
        else:
            print("Invalid input. Please try again. \n")
    print("Sea")


def on_the_rocks_scenario():
    """
    On the rocks
    """
    print("On the rocks")


def forest_clearing_scenario():
    """
    The user is back in the forest clearing from the intro but with a different decision.
    """
    print("------------------------------------------------------------------")
    print("Fuck that you say to yourself")
    print("You turn and run back into the woods")
    print("")
    print("")
    print("")
    print("You end up back where you were, in the clearing in the forest")
    print("What do you do? Go deeper into the forest or have a rest?")
    while play_game:
        decision = input("Go right into the forest or rest? forest / rest\n").strip().lower()
    if decision == "forest" or decision == "f":
        print("You go into the forest")
        forest_scenario()
    elif decision == "rest" or decision == "r":
        print("You sit down with your back to a tree and fall asleep")
        falling_asleep_scenario()
    else:
        print("Invalid input. Please try again. \n")


def falling_asleep_scenario():
    """
    Rest
    """
    print("You awake and its dark")

def forest_scenario():
    """
    Forest scenario
    """
    print("Forest")

intro()
