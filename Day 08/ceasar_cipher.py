#   importing module
import ceasar_cipher_art

#   letter stores all 26 alphabets
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#   encrypt encodes the text
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        #   checking if char is in the letter or not
        if char in letter:
            #   position stores position of current letter in text
            position = letter.index(char)
            #   new_position stores position of new letter
            new_position = (position + shift) % 26
            encrypted_text += letter[new_position]
        else:
            encrypted_text += char
    print(f"The encoded text is {encrypted_text}")

# decrypt decodes the text
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        #   checking if char is in the letter or not
        if char in letter:
            #   position stores position of current letter in text
            position = letter.index(char)
            #   new_position stores position of new letter
            new_position = (position - shift) % 26
            decrypted_text += letter[new_position]
        else:
            decrypted_text += char
    print(f"The decoded text is {decrypted_text}")

#   printing logo
print(ceasar_cipher_art.logo)

#   restart checks whether user wants to restart the program or not
restart = False

while not restart:
    #   taking input from User
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #   checking for valid direction and calling appropriate function
    if direction == "encode":
        encrypt(text=text, shift=shift)
    elif direction == "decode":
        decrypt(text=text, shift=shift)
    else:
        print("Invalid Direction.")
    
    #   asking user whether they want to restart the program or not
    choice = input("Type 'yes' if you want to restart, Otherwise type 'no'.\n").lower()
    if choice == "yes":
        restart = False
    else:
        restart = True
