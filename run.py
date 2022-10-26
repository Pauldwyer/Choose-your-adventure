# Global variable used to function loops and validation
PLAY_GAME = True

# Global variable for the username
USER_NAME = " "


def intro():
    """
    Introduction to the game.
    Asks user for their name and then greets the player.
    The name is validated for length, symbols and numbers using a while loop.
    If the name contains symbols or numbers the user is prompted to enter again.
    The user is then asked do they want to play a game.
    If the user answers yes then the start_game function is called.
    If the user answers no the the user is called a coward and
    the back_to_start function is called.
    A while loop evaluates user input.
    Only answers allowed are Yes, Y, No, N.
    Both user inputs is stripped of white space and converted into lowercase.
    """


    while PLAY_GAME:
        name = input("What is your name? \n").lower().strip()
        if len(name) < 1:
            print("Length of username is too short. Please try again.\n")
        elif len(name) > 20:
            print("Length of username is too long. Please try again.\n")
        elif all(char.isalpha() or char.isspace() for char in name):
            global USER_NAME
            USER_NAME = " ".join(name.split()).title()
            break
        elif any(char.isdigit() for char in name):
            print("Your name cannot contain a number. Please try again.\n")
        else:
            print("Your name cannot contain a symbol. Please try again.\n")

    print(f'Greetings {name.capitalize()}! \nWelcome to Pauls adventure game!')
    
    while PLAY_GAME:
        start = input("Would you like to play? Yes / No\n").lower().strip()
        if start == "yes" or start == "y":
            print("Great! lets play the game then")
            start_game()
            break
        elif start == "no" or start == "n":
            print("Coward!")
            back_to_start()
        else:
            print("Invalid input. Please try again. \n")

def back_to_start():
    """
    Asks the user do they want to go back to the start of the game
    If yes or y then the intro runs again
    If no or n the user exits the programme
    A while loop evaluates the user input
    User input is stripped of white space and converted into lowercase
    """
    while PLAY_GAME:
        to_the_start = input("Would you like to go back to the start? y/n \n").lower().strip()
        if to_the_start == "yes" or to_the_start == "y":
            intro()
        elif to_the_start == "no" or to_the_start == "n":
            exit()
        else:
            print("Invalid input. Please try again. \n")
    

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
    while PLAY_GAME:
        direction = input("Do you go left or right?\n").strip().lower()
        if direction == "left" or direction == "l":
            sea_scenario()
            break
        elif direction == "right" or direction == "r":
            forest_scenario()
            break
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
    print("You start to hear a lady singing")
    print("The sound of the voice is like an angel from heaven")
    print("You cant quite make out the words or language")
    print("You scan the beach and at the far you can make out a lady on the rocks")
    while PLAY_GAME:
        direction = input("Do you go forward and ask the lady for help or run back into the forest? Forward or back?\n").strip().lower()
        if direction == "forward" or direction == "f":
            on_the_rocks_scenario()
            break
        elif direction == "back" or direction == "b":
            forest_clearing_scenario()
            break
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
    while PLAY_GAME:
        decision = input("Go right into the forest or rest? forest / rest\n").strip().lower()
        if decision == "forest" or decision == "f":
            print("You go into the forest")
            forest_scenario()
            break
        elif decision == "rest" or decision == "r":
            print("You sit down with your back to a tree and fall asleep")
            falling_asleep_scenario()
            break
        else:
            print("Invalid input. Please try again. \n")


def falling_asleep_scenario():
    """
    Continues the story from when the user decides to rest.
    Gives a little back story to the story.
    This is a bad ending.
    Calls the bad_ending function.
    """
    print("------------------------------------------------------------------")
    print("")
    print("")
    print("'Dont hurt her' you shout")
    print("'Get back or else' you yell at the stranger")
    print("The stranger slowly steps towards you")
    print("He has a blade in one hand and a blackjack in the other")
    print("You turn to Emily and say 'Everything will be ok baby'")
    print("You turn again back to the stranger, he is edging closer slowly")
    print("'What do you want' you scream")
    print("")
    print("'You must pay for your transgressions' says the stranger in a lowly growl")
    print("You quickly grab the clock off the fireplace and you charge the stranger")
    print("")
    print("You swing with all your strength aiming for his head")
    print("")
    print("But he is too fast, he side steps your attemp and cracks you across the head with the blackjack")
    print("")
    print("You pass out")
    print("")
    print("You awake and find a bloody blade in your hand")
    print("You throw it across the floor, your hand is covered in blood")
    print("You look up and scan the room, you see Emily on the floor")
    print("She is covered in blood")
    print("")
    print("The door opens and Emilys father walks in")
    print("'What in the seven hells have you done' he shouts")
    print("")
    print("*Crack*")
    print("You awake with a splitting headache, you are back in the forest clearing")
    print("Your tied up against the tree")
    print("5 men looking down on you")
    print("You recognise Emilys father Pierre")
    print("'You thought you could runaway' he says 'Now you will die for what you did to my daughter'")
    print("'Do you have any last words?' Pierre says")
    print("As you open your mouth to protest Pierre slashes our throat")
    print("You bleed to death tied to the tree")
    bad_ending()


def bad_ending():
    """
    Bad ending function
    Will give some flavour text
    Will call the back to start function to start the game again
    """
    print("This is the bad ending")
    back_to_start()


def forest_scenario():
    """
    Forest scenario
    """
    print("Forest")

intro()
