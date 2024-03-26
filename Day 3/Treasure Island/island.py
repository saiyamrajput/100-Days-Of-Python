print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Hello! Welcome to Treasure Island!")

print("Your mission is to find the treasure.") 

first_choice = input('You are at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

if first_choice == "left":

    print("Great, you made it to the next level!!!")
    print("You got a treasure map")
    print('''
    ************************************************************
     _                                                           
    | |                                                          
    | |_ _ __ ___  __ _ ___ _   _ _ __ ___    _ __ ___   __ _ _ __  
    | __| '__/ _ \/ _` / __| | | | '__/ _ \  | '_ ` _ \ / _` | '_ \ 
    | |_| | |  __/ (_| \__ \ |_| | | |  __/  | | | | | | (_| | |_) |
    \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |  |_| |_|\__,_| .__/ 
                                                             | |    
                                                             |_|
    ***********************************************************
    ''')

    second_choice = input('According to the map there is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    
    if second_choice == "wait":
        
        print("You made it to the last stage.")
        third_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        
        if third_choice == "yellow":
            print("You found the treasure! You Win!")
        elif third_choice == "red":
            print("It's a room full of fire. Game Over.")
        elif third_choice == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")