# placeholder holds the string to replace
placeholder = "[name]"

# storing names in a list
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

# replacing placeholder with name
with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()

    # replacing names
    for i in names:
        # removing any extra space or lines
        i = i.strip()
        letters = content.replace(placeholder, i)

        # storing files
        with open(f"./Output/ReadyToSend/letter_for_{i}.txt", mode="w") as letter:
            letter.write(letters)
