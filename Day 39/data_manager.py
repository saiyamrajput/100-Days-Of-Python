# import statement
import requests

# creating sheety endpoint
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/*********/flightDeals/prices/"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Finds and returns Destination price"""

        # getting data from the API
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """Updates Destination codes"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
