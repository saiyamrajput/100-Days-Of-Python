# import statement
from coffee_machine_data import MENU, resources

# store the amount after selling the coffee
amount = 0


def print_report():
    """Prints all the details of the resources"""
    print(f"\nWater: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${amount}\n")


def check_resources(type_of_coffee):
    """Returns True when order can be made, False if ingredients 
    are insufficient, and displays appropriate message"""

    # item_is_available stores true if item is available otherwise false
    item_is_available = True

    # first checking if type of coffee is espresso or not
    if type_of_coffee == "espresso":
        # if yes then computing the following     
        if MENU[type_of_coffee]["ingredients"]["water"] > resources["water"]:
            print(f"\nThe amount of water required to make {type_of_coffee} is"
                  f" not sufficient.")
            item_is_available = False
        if MENU[type_of_coffee]["ingredients"]["coffee"] > resources["coffee"]:
            print(f"The amount of coffee required to make {type_of_coffee} is"
                  f" not sufficient.\n")
            item_is_available = False
    else:   # if type of coffee is not espresso
        if MENU[type_of_coffee]["ingredients"]["water"] > resources["water"]:
            print(f"\nThe amount of water required to make {type_of_coffee} is"
                  f" not sufficient.")
            item_is_available = False
        if MENU[type_of_coffee]["ingredients"]["coffee"] > resources["coffee"]:
            print(f"The amount of coffee required to make {type_of_coffee} is"
                  f" not sufficient.")
            item_is_available = False
        if MENU[type_of_coffee]["ingredients"]["milk"] > resources["milk"]:
            print(f"The amount of milk required to make {type_of_coffee} is"
                  f" not sufficient.\n")
            item_is_available = False

    return item_is_available


def subtract_resources(ingredients):
    """Subtracts the number of ingredients from the resources required to make
    the given type of coffee"""
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


def process_coins():
    """Returns the total amount received by the user from coins inserted."""

    # asking input from the user
    print("\nPlease insert the coins.\n")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    # calculating total amount
    total_amount = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05)
    total_amount += (pennies * 0.01)
    return total_amount


def coffee_machine():
    """Starting the Coffee Machine"""

    # on_off checks if machine is on or off
    on_off = False

    while not on_off:
        # asking users to choose coffee type
        choice = input("What would you like? "
                       "('espresso', 'latte', or 'cappuccino'). "
                       "Type corresponding Coffee name: ").lower()

        # checking for valid choice input
        if choice == "report":
            print_report()
        elif choice == "off":
            on_off = True
            print("\nTurning off the Machine")
        elif (choice == "espresso" or choice == "cappuccino"
              or choice == "latte"):

            # type stores the type of coffee
            coffee_type = MENU[choice]

            # first checking resources are available to make coffee or not
            if check_resources(choice):
                # if true then asking user to deposit the money
                money = process_coins()

                # now initializing payment and checking if it was a success
                #   or not
                if money < coffee_type["cost"]:
                    # if the amount is less the price of coffee
                    print("Sorry!! The Money provided is not enough. "
                          f"Your {money}$ has been refunded.\n")
                else:   # if amount is sufficient
                    global amount
                    amount += coffee_type["cost"]
                    # calculating change
                    left = round(money - coffee_type["cost"])
                    print(f"\nHere is ${left} in change.")

                    # making coffee
                    subtract_resources(coffee_type["ingredients"])
                    print(f"Here is your {choice} ☕️. Enjoy!! 😊\n")
        else:
            # restarting the machine
            print("\nInvalid choice!!\nRestarting the machine\n")


# starting the machine
coffee_machine()
