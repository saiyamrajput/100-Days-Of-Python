# import statements
import smtplib
import datetime as dt
import random
import pandas

# -------------------------------CHALLENGE------------------------------------ #

# Sending Monday morning quotes via email using Python

# # add your email and added app password below
# my_email = ""
# my_password = ""
#
# # storing today's weekday
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 0:
#     with open("quotes.txt") as quote_file:
#         quotes = quote_file.readlines()
#         random_quote = random.choice(quotes)
#
#     # connecting to the server
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(from_addr=my_email, to_addrs="",
#                             msg=f"Subject:Monday Motivation\n\n"
#                             f"Morning Quotes:\n{random_quote}")
#
# ---------------------------------------------------------------------------- #

# ------------------------------BIRTHDAY WISHER------------------------------- #

# add your email and added app password below
my_email = ""
my_password = ""

# reading today's date and time
now = dt.datetime.now()
today = (now.month, now.day)

# reading birthday's file and creating dictionary
data = pandas.read_csv("birthdays.csv")
data_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

# checking if today's date is matched with the birthdate or not
if today in data_dict:
    # extracting the birthday persons name
    bday_person = data_dict[today]

    # generating random letter
    letter = random.randint(1, 3)

    # extracting contents and renaming the name to the birthday persons name
    with open(f"./letter_templates/letter_{letter}.txt") as file:
        content = file.read()
        content = content.replace("[NAME]", bday_person["name"])

    # connecting to the server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="",
                            msg=f"Subject:Happy Birthday!\n\n"
                                f"{content}")
