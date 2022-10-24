def intro():
    """ 
    Introduction to the game.
    """
    print("Hi There")
    print("")
    name = input("Enter your name:   ")
    print(f'Greetings {name.capitalize()}! Welcome to Pauls adventure game!')
    start = input ("Would you like to play the game? Yes / No\n")


    if start.lower().strip() == "yes":
        print("Great! lets play the game then")
        start_game()
    else:
        print("Coward!")
        back_to_start()

def back_to_start():
    backToStart = input ("Would you like to go back to the start? y/n \n")
    if backToStart.lower().strip() == "yes":
        intro()
    else:
        exit()
    

def start_game():
    print("Starting the game")


intro()