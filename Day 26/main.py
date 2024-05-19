# import statement
import pandas

# reading the file
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# creating dictionary
data_dic = {code.letter: code.code for (index, code) in data.iterrows()}

# asking user for the input
word = input("Enter a word: ").upper()

# creating NATO alphabet
words = [data_dic[alphabet] for alphabet in word]

# printing the words
print(words)
