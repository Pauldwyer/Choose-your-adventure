#opening display for the game
def display():
    """
    Opening display title screen for the game
    
    """
    print("Welcome to Pauls choose your own adventure")
    answer = input("Do you wanna play? Yes / No")
    if answer.lower().strip() == "yes":
        start_game()
    else:
        print("Too bad")

display()