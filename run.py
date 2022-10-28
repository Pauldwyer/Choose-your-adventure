import os
# Imports stories functions from stories.py
from stories import *

# Global variable used to function loops and validation
PLAY_GAME = True

# Global variable for the username
username = " "


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
            global username
            username = " ".join(name.split()).title()
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
    Gives the user the first choice
    While loop to validate user input

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
            print("Invalid input. Please try again. \n")


def sea_scenario():
    """
    Story for when you take the direction of left in the forest clearing.
    Brings the user to a hidden beach
    Gives the user a choice to continue or go back to the forest.

    """
    sea_scenario_function(username)
    while PLAY_GAME:
        print("Do you go forward and ask for help or go back into the forest")
        direction = input("Forward or back?\n").strip().lower()
        if direction == "forward" or direction == "f":
            on_the_rocks_scenario()
            break
        elif direction == "back" or direction == "b":
            forest_clearing_scenario()
            break
        else:
            print("Invalid input. Please try again. \n")


def on_the_rocks_scenario():
    """
    On the rocks
    """
    on_the_rocks_function(username)
    bad_ending_function(username)
    back_to_start()


def forest_clearing_scenario():
    """
    The user is back in the forest clearing from the intro
    But with a different decision.
    """
    print("------------------------------------------------------------------")
    print("Fuck that you say to yourself")
    print("You turn and run back into the woods")
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
    falling_asleep_function(username)
    bad_ending()


def forest_scenario():
    """
    Forest scenario
    """
    forest_scene_function(username)
    while PLAY_GAME:
        decision = input("Hide or go ahead? hide/ahead \n").strip().lower()
        if decision == "hide" or decision == "h":
            cave_scenario()
            break
        elif decision == "ahead" or decision == "a":
            deeper_into_forest()
            break
        else:
            print("Invalid input. Please try again \n")


def cave_scenario():
    """
    Into the cave
    """
    cave_scenario_function(username)
    while PLAY_GAME:
        print("Do you go deeper into the cave or run?")
        decision = input("Deeper or Run?? /n").strip().lower()
        if decision == "deeper" or decision == "deep":
            deeper_into_cave_scene()
            break
        elif decision == "run" or decision == "r":
            running_out_of_cave_scene()
            break
        else:
            print("Invalid input. Please try again \n")


def deeper_into_cave_scene():
    """
    Venture deeper into the cave
    """
    deeper_into_cave_function(username)
    while PLAY_GAME:
        print("Quickly you must choose")
        decision = input("Sea, Forest or Back to the start?").strip().lower()
        if decision == "sea" or decision == "s":
            print("Tell her i sent you")
            on_the_rocks_scenario()
            break
        elif decision == "forest" or decision == "f":
            print("Good Choice")
            forest_scenario()
            break
        elif decision == "back" or decision == "b":
            print("Ah you played it safe")
            back_to_start()
        else:
            print("Invalid input. Please try sea, forest or back \n")


def deeper_into_forest():
    """
    Deeper into forest
    """
    print("Your right the cave is spooky, you march into the woods")


def bad_ending():
    """
    Bad ending function
    Will give some flavour text
    Will call the back to start function to start the game again
    """
    bad_ending_function(username)
    back_to_start()


intro()
