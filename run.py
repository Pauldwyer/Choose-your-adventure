# Imports stories functions from stories.py
from stories import *

# Import needed for clear terminal function
from os import system, name

# Global variable used to function loops and validation
PLAY_GAME = True

# Global variable for the username
username = " "


# Clear terminal function
# Taken from geeksforgeeks
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def intro():
    """
    Introduction to the game fucntion.
    Called to start the game loop.
    Asks user for input to assign variable username.
    Asks for another input
    Either 1 of 2 functions are called based on that input.
    All inputs stripped of whitespace and coverted to lowercase.
    All inputs validated with while loop.
    """

    typewriter_title("""
 ______  __ __    ___      __    __   ___    ___   ___   _____
|      ||  |  |  /  _]    |  |__|  | /   \  /   \ |   \ / ___/
|      ||  |  | /  [_     |  |  |  ||     ||     ||    (   \_ 
|_|  |_||  _  ||    _]    |  |  |  ||  O  ||  O  ||  D  \__  |
  |  |  |  |  ||   [_     |  `  '  ||     ||     ||     /  \ |
  |  |  |  |  ||     |     \      / |     ||     ||     \    |
  |__|  |__|__||_____|      \_/\_/   \___/  \___/ |_____|\___|
    """)

    typewriter("""
    Welcome to The Woods
    An Interactive Story by Paul Dwyer

    How to play do you ask?

    The story will be told in sections and at the end of each section,
    You will be given a choice.
    How you choose has consequences for how the story unfolds.

    Can you make it to the end of The Woods?

    Before we start please tell me one thing.
    \n""")

    while PLAY_GAME:
        name = input("    What is your name? \n").lower().strip()
        if len(name) < 1:
            print("    Length of username is too short. Please try again.\n")
        elif len(name) > 20:
            print("    Length of username is too long. Please try again.\n")
        elif all(char.isalpha() or char.isspace() for char in name):
            global username
            username = " ".join(name.split()).title()
            break
        elif any(char.isdigit() for char in name):
            print("    Your name cannot contain a number. Please try again.\n")
        else:
            print("    Your name cannot contain a symbol. Please try again.\n")

    print(f"    Greetings {name.capitalize()}!")

    while PLAY_GAME:
        start = input("    Would you like to play? Yes / No \n").lower().strip()
        if start == "yes" or start == "y":
            print("    Great! lets go!")
            clear()
            start_game()
            break
        elif start == "no" or start == "n":
            print("    Coward!")
            clear()
            back_to_start()
        else:
            print("    Invalid input. Please try again. \n")


def back_to_start():
    """
    Back to start function.
    Takes user input.
    Calls either 1 of 2 functions based on input.
    While loop validates input.
    User input is stripped of white space and converted into lowercase.
    """
    while PLAY_GAME:
        print("\n    Would you like to go back to the start?")
        decision = input("\n    Yes or No \n")
        if decision == "yes" or decision == "y":
            clear()
            intro()
        elif decision == "no" or decision == "n":
            exit()
        else:
            print("    Invalid input. Please try Yes or No.\n")


def start_game():
    """
    Start game function. Starts the story.
    Takes user input.
    Calls either 1 of 2 functions based on input.
    User input is stripped of white space and converted into lowercase.
    While loop to validate user input.
    """
    start_game_function()
    print("What do you do?")
    while PLAY_GAME:
        direction = input("    Do you go left or right?\n    ").strip().lower()
        if direction == "left" or direction == "l":
            sea_scenario()
            break
        elif direction == "right" or direction == "r":
            forest_scenario()
            break
        else:
            print("    Invalid input. Please try Left or Right.\n")


def sea_scenario():
    """
    Sea scenario function
    Clears the terminal.
    Takes user input.
    Calls either 1 of 2 functions based on input.
    User input is stripped of white space and converted into lowercase.
    While loop to validate user input.
    """
    clear()
    sea_scenario_function(username)
    while PLAY_GAME:
        print("\n    Go forward and ask for help or go back into the forest?")
        direction = input("    Forward or back?\n").strip().lower()
        if direction == "forward" or direction == "f":
            on_the_rocks_scenario()
            break
        elif direction == "back" or direction == "b":
            forest_clearing_scenario()
            break
        else:
            print("    Invalid input. Please try Forward or Back.\n")


def on_the_rocks_scenario():
    """
    On the rocks scenario function
    Clears the terminal.
    Calls 3 functions in order.
    Gives user story, the bad ending and ask do they want to start again.
    """
    clear()
    on_the_rocks_function(username)
    bad_ending_function(username)
    back_to_start()


def forest_clearing_scenario():
    """
    Forest clearing scenario.
    Clears the terminal.
    Takes user input.
    Calls either 1 of 2 functions based on input.
    User input is stripped of white space and converted into lowercase.
    While loop to validate user input.
    """
    clear()
    forest_clearing_function()
    while PLAY_GAME:
        decision = input("    Forest or Rest\n").strip().lower()
        if decision == "forest" or decision == "f":
            forest_scenario()
            break
        elif decision == "rest" or decision == "r":
            falling_asleep_scenario()
            break
        else:
            print("    Invalid input. Please try Forest or Rest.\n")


def falling_asleep_scenario():
    """
    Falling asleep scenario.
    Clears the terminal.
    Calls 2 functions in order.
    Bad ending.
    """
    clear()
    falling_asleep_function(username)
    bad_ending()


def forest_scenario():
    """
    Forest scenario
    Clears the terminal.
    Takes user input.
    Calls either 1 of 2 functions based on input.
    User input is stripped of white space and converted into lowercase.
    While loop to validate user input.
    """
    clear()
    forest_scene_function(username)
    while PLAY_GAME:
        decision = input("\n    Hide or go ahead?\n").strip().lower()
        if decision == "hide" or decision == "h":
            cave_scenario()
            break
        elif decision == "ahead" or decision == "a":
            deeper_into_forest()
            break
        else:
            print("    Invalid input. Please try Hide or Ahead \n")


def cave_scenario():
    """
    Into the cave scenario
    Clears the terminal.
    Takes user input.
    Calls either 1 of 2 functions based on input.
    User input is stripped of white space and converted into lowercase.
    While loop to validate user input.
    """
    clear()
    cave_scenario_function(username)
    while PLAY_GAME:
        decision = input("    Deeper or Run?? \n").strip().lower()
        if decision == "deeper" or decision == "deep":
            deeper_into_cave_scene()
            break
        elif decision == "run" or decision == "r":
            running_out_of_cave_scene()
            break
        else:
            print("    Invalid input. Please try Deeper or Run.\n")


def running_out_of_cave_scene():
    """
    Running out of the cave.
    Clears the terminal.
    Calls 1 function from stories.py
    Calls the bad ending function.
    """
    clear()
    running_out_of_cave_function()
    bad_ending()


def deeper_into_cave_scene():
    """
    deeper into the cave scene
    Clears the terminal
    Takes user input.
    Calls either 1 of 3 functions based on input.
    User input is stripped of white space and converted into lowercase.
    While loop to validate user input.
    """
    clear()
    deeper_into_cave_function(username)
    while PLAY_GAME:
        print("    Quickly you must choose")
        decision = input("    Sea, Forest or Back to the start?").strip().lower()
        if decision == "sea" or decision == "s":
            print("    Tell her i sent you")
            on_the_rocks_scenario()
            break
        elif decision == "forest" or decision == "f":
            print("    Good Choice")
            forest_scenario()
            break
        elif decision == "back" or decision == "b":
            print("    Ah you played it safe")
            back_to_start()
        else:
            print("    Invalid input. Please try Sea, Forest or Back \n")


def deeper_into_forest():
    """
    Deeper into forest
    Clears the terminal
    Takes user input.
    Calls either 1 of 2 functions based on input.
    User input is stripped of white space and converted into lowercase.
    While loop to validate user input.
    """
    clear()
    deeper_into_forest_function(username)
    while PLAY_GAME:
        decision = input("    Fight or Run?? \n").strip().lower()
        if decision == "fight" or decision == "f":
            stand_and_fight()
            break
        elif decision == "run" or decision == "r":
            run_from_dogs()
            break
        else:
            print("    Invalid input. Please try Fight or Run \n")


def stand_and_fight():
    """
    Fight the dogs
    Clears the terminal
    Takes user input.
    Calls either 1 of 2 functions based on input.
    User input is stripped of white space and converted into lowercase.
    While loop to validate user input.
    """
    clear()
    stand_and_fight_function(username)
    while PLAY_GAME:
        decision = input("    Portal or Run?? \n").strip().lower()
        if decision == "portal" or decision == "p":
            into_the_portal()
            break
        elif decision == "run" or decision == "r":
            run_from_portal()
            break
        else:
            print("    Invalid input. Please try Portal or Run\n")


def run_from_dogs():
    """
    Run from dogs.
    Clears the terminal
    Calls 1 functions from stories.py.
    Calls Bad ending function.
    """
    clear()
    run_from_dogs_function()
    bad_ending()


def run_from_portal():
    """
    Run from portal function.
    Clears the terminal
    Calls 1 function from stories.py
    Calls bad ending function.
    """
    clear()
    run_from_portal_function()
    bad_ending()


def into_the_portal():
    """
    Into the portal scene
    Clears the terminal
    Calls 1 function from stories.py.
    Calls back to start function.
    """
    clear()
    into_the_portal_function()
    back_to_start()


def bad_ending():
    """
    Bad ending function.
    Clears the terminal
    Calls 1 from function from stories.py.
    Calls back to start function.
    """
    clear()
    bad_ending_function(username)
    back_to_start()


# Starts the game loop
intro()
