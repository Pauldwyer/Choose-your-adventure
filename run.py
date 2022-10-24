
def intro():
    """ 
    Introduction to the game.
    """
    name = input("Enter your name:   ")
    print(f'Greetings {name.capitalize()}! Welcome to Pauls adventure game!')
    start = input ("Would you like to play the game? Yes / No\n")


    if start.lower().strip() == "yes":
        print("Great! lets play the game then")
        start_game()
    else:
        print("Thats too bad!")
        quit()

def quit():
    print("That")
    intro()

def start_game():
    print("Starting the game")


intro()