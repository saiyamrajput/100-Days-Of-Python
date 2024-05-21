import random

#   importing the modules hangman_words and hangman_art
import hangman_words
import hangman_art

#   chosing random word from word_list
chosen_word = random.choice(hangman_words.word_list)

#   calculating length of chosen_word
word_length = len(chosen_word)

#   end_of_game helps us decide whether game ended or not
end_of_game = False

#   lives stores the number of times we can guess word if
#       guess of letter is wrong
lives = 6

#   printing hangman logo
print(hangman_art.logo)

#   creating blanks
word = []
for i in range(word_length):
    word += "_"

#   playing the game
while not end_of_game:
    #   asking user to input the guess
    guess = input("Guess a letter: ").lower()

    #   checking if user has already gussed the word or not 
    if guess in word:
        print(f"You have already guessed the word")

    #   Checking guessed letter
    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            word[i] = letter

    #   Checking if user is wrong.
    if guess not in chosen_word:
        # if the guess is not in the word, then printing appropriate message
        print(f"Your guess '{guess}' is not in the word ")
        #   decrementing lives
        lives -= 1
        #   checking if user has anymore live or not
        if lives == 0:
            end_of_game = True
            print(f"The word was '{chosen_word}' ")
            print("You lose.")

    #   joining all the elements in the list and turning it into a String.
    print(f"{' '.join(word)}")

    #   checking if user has got all letters.
    if "_" not in word:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
