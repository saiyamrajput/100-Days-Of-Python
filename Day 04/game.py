#import statement
import random

# storing rock, paper and scissors value in the variables below
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# storing rock paper scissors in images
images = [rock, paper, scissors]
# taking input from the user
choice = int(
    input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# randomly generating computer choice
computer_choice = random.randint(0, 2)

# checking who won the game if input is valid
if choice == 0:     # when user chose rock
    # printing user's choice image
    print(rock)
    # prinitng computers choice image
    print(f"Computer chose: {computer_choice}")
    print(images[computer_choice])
    # checking for win condition
    if computer_choice == 0:
        print("It's a draw")
    elif computer_choice == 1:
        print("You lose")
    else:
        print("You win!")
elif choice == 1:   # when user chose paper
    # printing user's choice image
    print(paper)
    # prinitng computers choice image
    print(f"Computer chose: {computer_choice}")
    print(images[computer_choice])
    # checking for win condition
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("It's a draw")
    else:
        print("You lose")
elif choice == 2:  # when use chose scissors 
    # printing user's choice image
    print(scissors)
    # prinitng computers choice image
    print(f"Computer chose: {computer_choice}")
    print(images[computer_choice])
    # checking for win condition
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("It's a draw")
else:   # checking for invalid case
    print("Invalid user choice, you lose")
