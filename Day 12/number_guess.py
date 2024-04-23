#   import statements
import number_guess_art
import random
import os

#====global variables========================================================

#   easy stores number of turns available at easy difficulty
easy = 10

#   hard stores number of turns available at hard difficulty
hard = 5

#===functions================================================================

def clear():
    """Clears the screen on call"""
    if os.name == 'nt':  # checking if the OS is Windows
        os.system('cls')
    else:
        os.system('clear')

#   check function checks whether guess is too low or too high or correct
def check(guess, ans, turn):
    """Checks if guess is correct or not and returns number of turns left"""
    
    #   checking if user gussed the number correct or not
    if guess > ans:
        print("Guess is too high \U0001F976")
        return turn - 1
    elif guess < ans:
        print("Guess is too low \U0001F976")
        return turn - 1
    else:
        print(f"You got it \U0001F60E \U0001F389. The correct answer is: "
              f"{ans}")
        return -1

#   game_level function sets game difficulty
def game_level(choice):
    """Returns the number of turns according to difficulty of game"""
    
    #   checking for users choice
    if choice == "easy":
        return easy
    elif choice == "hard":
        return hard
    else:
        print("\nInvalid difficulty level\n")
        return 0

# start of game
def number_guess():
    """Start of the game"""

    #   printing logo
    print(number_guess_art.logo)
    #   welcome message
    print("Welcome to the Number Guessing Game!!!!\n")
    print("I am thinking of number between 1 and 100.\n")

    #   asking user for difficulty level
    print("Choose a difficulty level:\n1. Easy\n2. Hard\n")
    level = input("Type 'easy' or 'hard' to choose difficulty level: ").lower()

    #   randomly generating number between 1 and 100
    num = random.randint(1, 100)

    #   setting number of turns according to difficulty level chosen by user
    turn = game_level(level)
    
    #   checking if level is valid or not
    if turn != 0: 
        print(f"\nYou have {turn} attempts to guess the number.\n")
        
        #   game_over checks if game is finished or not
        game_over = False

        while not game_over:
            #   asking user to input their guess
            guess = int(input("Make a guess: "))

            #   checking if guess is right or not
            turn = check(guess, num, turn)

            #   checking if user won or not
            if turn == -1:
                print("\n-------------Game Over-------------\n")
                game_over = True
            elif turn <= 0:
                print("\nYou have run out of turn and you lost")
                print(f"The correct answer was: {num}")
                print("\n-------------Game Over-------------\n")
                game_over = True
            else:
                print("\nGuess again.")
                print(f"\nYou have {turn} attempts to guess the number.\n")


#   asking user if he wants to play the game or not
choice = input("Type 'yes' if you want to play Number Guessing Game,"
               " Otherwise type anyhting to quit:\n")

while choice == "yes":
    clear()
    #   starting the game
    number_guess()

    #   asking user if he wants to continue playing or not
    choice = input("Type 'yes' if you want to continue playing,"
                   " Otherwise type anyhting to quit:\n")
