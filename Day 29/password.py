# importing random module
import random


class Password:

    def __init__(self):
        self.password = ""
        self.hard_password = []

        #   storing alphabets, numbers, and symbols required for password in
        #       letters,numbers and symbols
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                        'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def generate(self):
        #   storing all the letters first
        for i in range(random.randint(8, 10)):
            random_value = random.randint(0, len(self.letters) - 1)
            self.hard_password.append(self.letters[random_value])

        #   storing all the symbols
        for i in range(random.randint(2, 4)):
            random_value = random.randint(0, len(self.symbols) - 1)
            self.hard_password.append(self.symbols[random_value])

        #   storing all the numbers
        for i in range(random.randint(8, 10)):
            random_value = random.randint(0, len(self.numbers) - 1)
            self.hard_password.append(self.numbers[random_value])

        #   shuffling the hard password using shuffle
        random.shuffle(self.hard_password)

        #   storing password in password from list to string
        for i in self.hard_password:
            self.password += i

        return self.password
