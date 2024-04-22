#   import statements
import calculator_art
import os

#   add function
def add(num1, num2):
    """Takes two number as input and returns their sum."""
    return num1 + num2

#   subtract function
def subtract(num1, num2):
    """Takes two number as input and returns their difference."""
    return num1 - num2

#   multiplication function
def mult(num1, num2):
    """Takes two number as input and returns their product."""
    return num1 * num2

#   division function
def div(num1, num2):
    """Takes two number as input and returns their quotient."""
    return num1 / num2

def calculator():
    """Performs all the calculations"""
    #   printing starting logo
    print(calculator_art.logo)

    #   taking input
    num1 = float(input("Enter the first number: "))

    #   printing operators
    print("\nSelect a operator:")
    print(f"+\n-\n*\n/")

    #  checks whether user wants to carry with the same number to perform
    #      operation or start a fresh operation
    continue_operation = False
    result = 0

    #   calculating values below
    while not continue_operation:
        #   taking input of the operator
        op = input("\nWhat operation do you want to perform?: ")
        #   taking input of another number
        num2 = float(input("\nEnter another number: "))

        #   checking which operation to perform according to op
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = mult(num1, num2)
        elif op == "/":
            #   checking for 0/0 error
            if num2 == 0:
                print("Undefined error: division by 0\n")
                result = 0
            else:
                result = div(num1, num2)
        else:
            print(f"The selected operator '{op}' is invalid")
            exit()
    
        #   printing result
        print("\nCalculating result...\n")
        print(f"Result: {num1} {op} {num2} = {result}\n")

        #   asking user if they want to continue with same result or not
        continue_op = input(f"Do you want to continue calculating with '{result}'?"
                            f"\nIf yes then please type 'yes', otherwise type 'no'"
                            f" to start fresh calculation"
                            f"\nOr, type anything to exit: \n").lower()

        if continue_op == "yes":
            print(f"\nPrevious result value is: {result}")
            num1 = result
            #   printing operators
            print("\nSelect a operator:")
            print(f"+\n-\n*\n/")
        elif continue_op == "no":
            #   performing necessary operations if users inputs "no"
            #   first clearing the screen
            if os.name == 'nt':  # checking if the OS is Windows
                os.system('cls')
            else:
                os.system('clear')
            #   after clearing the screen restarting the program
            calculator()
        else:
            continue_operation = True
            exit()

#   starting calculator
calculator()
