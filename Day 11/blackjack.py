#   import statement
import blackjack_art
import random
import os

def clear():
    """Clears the screen on call"""
    if os.name == 'nt':  # checking if the OS is Windows
        os.system('cls')
    else:
        os.system('clear')

def total_value(cards):
    """Returns sum of all the values in list."""
    s = 0
    #   length stores the length of cards
    length = len(cards)
    #   for loop calculates sum of the values
    for i in range(length):
        s += cards[i]
    return s

def deal():
    """Returns a random card from 'cards'."""
    #   cards stores card values
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def score_cal(cards):
    """Returns the total value(summation) of cards"""

    #   value stores sum of all the elements of cards
    value = total_value(cards)
    #   cards_len stores length of cards
    cards_len = len(cards)
    if value == 21 and cards_len == 2:  #   checking for blackjack
        return 0    #   returning 0 if it is a blackjack
    
    #   checking if 11 is in card and value > 21, then removing 11
    #       from cards and adding 1
    if 11 in cards and value > 21:
        cards.remove(11)
        cards.append(1)
        value = total_value(cards)
    return value

#   comparison function compares the scores of both user and comp
def comparison(user, comp):
    """Compares the given scores and returns the result of the game"""
    
    #   if both players have card values(summation) > 21
    if user > 21 and comp > 21 :
        return "You went over 21 and lost \U0001F972 \U0001F62D"
    
    if user == comp:
        return "Draw \U0001F972 \U0001F643"
    elif comp == 0:
        return "You lost, opponent has BlackJack and won the game \U0001F976"
    elif user == 0:
        return "You win with a BlackJack \U0001F60E \U0001F389"
    elif user > 21:
        return "You went over 21 and lost \U0001F972 \U0001F62D"
    elif comp > 21:
        return "Opponent went over 21 and you win \U0001F62F \U0001F910"
    elif user > comp:
        return "You win \U0001F601"
    else:
        return "You lose \U0001F62D \U0001F62D"


def blackjack():
    """Starting of Game"""
    #   printing logo
    print(blackjack_art.logo)

    #   end_game tracks whether the game ended or not
    end_game = False

    #   user_card stores users card and comp_card stores computers card
    users_card = []
    comp_card = []

    #   storing random card values in user_card and comp_card
    for i in range(2):
        users_card.append(deal())
        comp_card.append(deal())

    #   playing the game
    while not end_game:
        #   calculating users_card and comp_card total sum in user and comp
        user = score_cal(users_card)
        comp = score_cal(comp_card)

        #   printing users_card, user, and comp_card (comp_card first value only)
        print(f"\nYour Cards: {users_card}\nYour current score is: {user}")
        print(f"Computer's first Card is: {comp_card[0]}")

        #   checking if game ended or not
        if comp == 0 or user == 0 or user > 21:
            end_game = True
        else:   #   if game is not ended
            draw_card = input("\nIf you want to draw another card type 'yes',"
                            " otherwise type anything to pass: \n").lower()
            #   checking users choice
            if draw_card == "yes":
                users_card.append(deal())
            else:
                end_game = True

    #   checking if computer can draw anymore cards or not, i.e., computers
    #       turn to play
    while comp < 17 and comp != 0:
        comp_card.append(deal())
        comp = score_cal(comp_card)

    #   printing final cards of both user and computer and the winner
    print(f"\nYour final hand: {users_card},\nYour final score is: {user}")
    print(f"Computer's final hand: {comp_card},"
          f"\nComputer's final score: {comp}")
    print(comparison(user, comp))

#   starting the game by asking user if the user wants to play the game or not
choice = input("Type yes to play BlackJack,"
               " otherwise type anyhting:\n").lower()

#   checking if user wants to play the game again or not
while choice == "yes":
    clear()
    blackjack()
    choice = input("\nType yes to play BlackJack,"
                   " otherwise type anyhting:\n").lower()
