print("Hello! Welcome to the Tip Calculator!")
bill = float(input("What is your total bill? $"))
tip_rate = int(input
        ("How much percentage of tip would you like to give: 10, 12 or 15? "))
persons = int(input("How many people will split the bill? "))
total_amount = (bill + (bill * (tip_rate / 100))) / persons
total_amount = round(total_amount, 2)
print(f"You need to pay ${total_amount} per person")