# import statements
import os
import secret_auction_art

# highest_bid checks which user has the highest bidding amount
def highest_bid(bidding):
  # max_bid stores highest bid value
  max_bid = 0
  # win stores the name of the highest bidder
  win = ""
  # checking for highest bidder and max bid amount
  for user in bidding:
    amount = bidding[user]
    if amount > max_bid: 
      max_bid = amount
      win = user
  print(f"The highest bid is ${max_bid} by the person '{win}' ")

# printing logo
print(secret_auction_art.logo)

# users_bids stores users name and their bids
users_bids = {}

# bidding_over helps to check whether bidding is over or not
bidding_over = False

# bidding starts
while not bidding_over:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  users_bids[name] = price
  # proceed stores the user input to whether proceed with the auction or not
  proceed = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
  
  # checking if user wants to proceed or not then performing necessary operations
  if proceed == "yes":
    if os.name == 'nt':  # checking if the OS is Windows
      os.system('cls')
    else:
      os.system('clear')
  elif proceed == "no":
    bidding_over = True
    highest_bid(users_bids)
