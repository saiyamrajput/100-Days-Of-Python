# import statement
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# object for ordering drinks
menu = Menu()

# object for printing report of all resources, and if they are sufficient or not
coffee_maker = CoffeeMaker()

# object for printing report and initializing payment from the user and to check
#   if it was successful or not
money_machine = MoneyMachine()


def coffee_machine():
    """Starting the Coffee Machine"""

    # coffee_type stores the available coffee names the machine can make
    coffee_type = menu.get_items()

    # on_off checks if machine is on or off
    on_off = False
    while not on_off:
        # asking users to choose coffee type
        choice = input("What would you like? "
                       f"('{coffee_type}'). "
                       "Type corresponding Coffee name: ").lower()

        # checking for valid choice input
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == "off":
            on_off = True
            print("\nTurning off the Machine")
        elif (choice == "espresso" or choice == "cappuccino"
              or choice == "latte"):

            # store the coffee type
            coffee = menu.find_drink(choice)

            # checking if resources are available to make coffee and payment
            #   made by user is sufficient or not
            if (coffee_maker.is_resource_sufficient(coffee) and
                    money_machine.make_payment(coffee.cost)):
                coffee_maker.make_coffee(coffee)
        else:
            # restarting the machine
            print("\nInvalid choice!!\nRestarting the machine\n")


# starting the machine
coffee_machine()
