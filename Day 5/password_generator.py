# importing random module
import random

#   storing alphabets, numbers, and symbols required for password in letters,
#       numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#   printing the greeting and taking input from the user
print("Hello! Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#   variable to store easy password
easy_password = ""

#   storing all the letters first
for i in range(0, nr_letters):
    random_value = random.randint(0, 51)
    easy_password += letters[random_value]

#   storing all the symbols
for i in range(0, nr_symbols):
    random_value = random.randint(0, 8)
    easy_password += symbols[random_value]

#   storing all the numbers
for i in range(0, nr_numbers):
    random_value = random.randint(0, 9)
    easy_password += numbers[random_value]

#   printing easy password
print("Generating easy password...")
print("Easy password is: " + easy_password)

#   printing an extra line
print()


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#   variable to store hard password
hard_password = []

#   storing all the letters first
for i in range(0, nr_letters):
    random_value = random.randint(0, 51)
    hard_password.append(letters[random_value])

#   storing all the symbols
for i in range(0, nr_symbols):
    random_value = random.randint(0, 8)
    hard_password.append(symbols[random_value])

#   storing all the numbers
for i in range(0, nr_numbers):
    random_value = random.randint(0, 9)
    hard_password.append(numbers[random_value])

#   shuffling the hard password using shuffle
random.shuffle(hard_password)

#   prinitng the hard password
print("Generating hard password...")

#   storing hard password in password from list to string
password = ""
for i in hard_password:
    password += i

print("Hard password is: " + password)

#   printing an extra line
print()