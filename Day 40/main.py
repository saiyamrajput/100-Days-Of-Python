# import statements
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import sheety

# # ----------------------USER INFORMATION-------------------------------------- #
#
# print("Welcome to the Flight Club.\n We find the best flight deals "
#       "and email them to you.")
#
# # asking user for input
# first_name = input("What is your first name? ").title()
# last_name = input("What is your last name? ").title()
#
# email1 = "email1"
# email2 = "email2"
# while email1 != email2:
#     email1 = input("What is your email? ")
#     if email1.lower() == "quit" \
#             or email1.lower() == "exit":
#         exit()
#     email2 = input("Please verify your email : ")
#     if email2.lower() == "quit" \
#             or email2.lower() == "exit":
#         exit()
#
# print("OK. You're in the club!")
# sheeety.post_new_row(first_name, last_name, email1)
#
# # ---------------------------------------------------------------------------- #

# creating objects
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# adding original city IATA
ORIGIN_CITY_IATA = "LON"

# checking if IATA code is not in the sheet
if sheet_data[0]["iataCode"] == "":
    # getting city names
    city_names = []
    for row in sheet_data:
        city_names.append(row["city"])
    # getting destination codes
    data_manager.city_codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

# creating destinations dictionary
destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

# generating tomorrow's date and the date six months from today
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# checking for destination in sheet data
for destination_code in destinations:
    # searching for flights
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    # printing flight price
    print(flight.price)

    # if flight is not available then continuing
    if flight is None:
        continue

    # checking cheap price
    if flight.price < destinations[destination_code]["price"]:
        # getting user information
        user = data_manager.get_customer_emails()
        emails = [row["email"] for row in user]
        names = [row["firstName"] for row in user]

        # generating message
        message = (f"Low price alert! Only £{flight.price} to fly from "
                   f"{flight.origin_city}-{flight.origin_airport} to "
                   f"{flight.destination_city}-{flight.destination_airport}, "
                   f"from {flight.out_date} to {flight.return_date}.")

        # checking for any flight stops
        if flight.stop_overs > 0:
            # updating message
            message += (f"\nFlight has {flight.stop_overs} stop over, "
                        f"via {flight.via_city}.")

        # sending message
        notification_manager.send_message(emails, message)
