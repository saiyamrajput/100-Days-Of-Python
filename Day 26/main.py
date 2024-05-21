# import statement
import pandas

# reading the file
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# creating dictionary
data_dic = {code.letter: code.code for (index, code) in data.iterrows()}


def generate():
    """Generates Phonetic words"""
    # asking user for the input
    word = input("Enter a word: ").upper()

    # handling error
    try:
        # creating NATO alphabet
        words = [data_dic[alphabet] for alphabet in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate()
    else:
        # printing the words
        print(words)


generate()
