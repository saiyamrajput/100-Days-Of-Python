# import statements
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# creating objects
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# adding original city IATA
ORIGIN_CITY_IATA = "LON"

# checking if IATA code is not in the sheet
if sheet_data[0]["iataCode"] == "":
    # if yes then updating the sheet
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# generating tomorrow's date and the date six months from today
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# checking for destination in sheet data
for destination in sheet_data:
    # searching for flights
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    # checking cheap price
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_message(
            message=f"Low price alert! Only £{flight.price} to fly from "
                    f"{flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.destination_city}-{flight.destination_airport}, "
                    f"from {flight.out_date} to {flight.return_date}."
        )
