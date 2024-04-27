#   import statements
import os
import higher_lower_game_arts
import higher_lower_game_data
import random



def clear():
    """Clears the screen on call"""
    if os.name == 'nt':  # checking if the OS is Windows
        os.system('cls')
    else:
        os.system('clear')

def print_format(acc):
    """Prints the account details in proper format: name, description and
       country"""
    name = acc["name"]
    description = acc["description"]
    country = acc["country"]
    return f"{name}, a {description}, from {country}."

def correct_choice(choice, acc1, acc2):
    """Returns true if the user guess is right, otherwise returns false"""
    #   checking which account has more followers, then performing comparison
    if acc1["follower_count"] > acc2["follower_count"]:
        return choice == "A"
    else:
        return choice == "B"

def higher_lower_game():
    """Start of game"""

    #   generating random account
    acc1 = random.choice(higher_lower_game_data.data)
    acc2 = random.choice(higher_lower_game_data.data)

    #   printing logo
    print(higher_lower_game_arts.logo)
    #   welcome message
    print("Welcome to the Higher Lower Game!!!!\n")

    #   game_over checks if game is finished or not
    game_over = False

    # num stores total points earned while playing the game
    num = 0

    #   Playing the game
    while not game_over:
        #   copying the value of acc2 to acc1, and then generating
        #       new data for acc2
        acc1 = acc2
        acc2 = random.choice(higher_lower_game_data.data)

        #   checking if both account are same then changing acc2
        while acc1 == acc2:
            acc2 = random.choice(higher_lower_game_data.data)
        
        #   printing acc1 and acc2
        print(f"Compare A: {print_format(acc1)}\n")
        print(higher_lower_game_arts.vs)
        print(f"\nAgainst B: {print_format(acc2)}\n")

        #   asking user for their choice
        choice = input("Who has more followers? Type 'A' or 'B':\n").upper()

        #   checking for valid choice
        if choice == "A" or choice == "B":
            #   checking if the guess was right or not
            win = correct_choice(choice, acc1, acc2)

            #   checking if user won the game or not
            if win:
                clear()
                #   printing logo
                print(higher_lower_game_arts.logo)
                num += 1
                #   printing score details
                print(f"\nYou are right!!! Your current score is: {num}\n")
            else:   #   if game lost
                clear()
                game_over = True
                print("Sorry you lost the game.\n")
                print(f"Your Final score is: {num}\n")
        else:
            clear()
            print("You entered wrong choice\n")
            game_over = True

#   asking user if he wants to play the game or not
choice = input("Type 'yes' if you want to play Higher Lower Game,"
               " Otherwise type anyhting to quit:\n").lower()

while choice == "yes":
    clear()
    #   starting the game
    higher_lower_game()

    #   asking user if he wants to continue playing or not
    choice = input("Type 'yes' if you want to continue playing,"
                   " Otherwise type anyhting to quit:\n").lower()
